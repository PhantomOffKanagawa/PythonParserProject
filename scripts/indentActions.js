"use strict";

// Initialize state
let tokens = [];
let indents = [];
let mIndent = -1;
let lastToken = null;

// Helper functions
function emit(token) {
    if (!token) {
        // Create default token if none provided
        token = this._factory.create(
            this._tokenFactorySourcePair,
            this._type,
            this._text,
            this._channel,
            this._tokenStartCharIndex,
            this.getCharIndex()-1,
            this._tokenStartLine,
            this._tokenStartColumn
        );
    }
    this._token = token;
    tokens.push(token);
    return token;
}

function createDedent() {
    const dedent = {
        type: this.DEDENT,
        channel: this.DEFAULT_TOKEN_CHANNEL,
        start: this.getCharIndex()-1,
        stop: this.getCharIndex()-1,
        line: lastToken.line,
        text: "<DEDENT>"
    };
    return dedent;
}

function createIndent() {
    const indent = {
        type: this.INDENT, 
        channel: this.DEFAULT_TOKEN_CHANNEL,
        start: this.getCharIndex()-1,
        stop: this.getCharIndex()-1,
        line: lastToken.line,
        text: "<INDENT>"
    };
    return indent;
}

function commonToken(type, text) {
    const stop = this.getCharIndex() - 1;
    const start = text.length === 0 ? stop : stop - text.length + 1;
    return {
        type: type,
        channel: this.DEFAULT_TOKEN_CHANNEL,
        start: start,
        stop: stop,
        text: text
    };
}

function getIndentationCount(spaces) {
    let count = 0;
    for (let i = 0; i < spaces.length; i++) {
        if (spaces[i] === '\t') {
            count += 4 - (count % 4);
        } else {
            count++;
        }
    }
    return count;
}

function atStartOfInput() {
    return this.column === 0 && this.line === 1;
}