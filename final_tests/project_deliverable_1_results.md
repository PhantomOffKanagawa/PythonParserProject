![Deliverable 1 Parse Tree](./deliverable_1.svg)
> Image at `./final_tests/deliverable_1.svg`
> Secondary Image at `./final_tests/project_deliverable_1_parse_tree.png`

```
(popl) $ python ./scripts/combine_grammars.py && antlr4 -Dlanguage=Python3 ./grammars/FullLexer.g4 ./grammars/FullParser.g4 && python main.py
Generated grammar files. Compile with:
antlr4 -Dlanguage=Python3 ./grammars/FullLexer.g4 ./grammars/FullParser.g4
Tokenizing ./final_tests/project_deliverable_1.py:
[@0,0:6='assign1',<29>,1:0] VARIABLE
[@1,7:7=' ',<30>,1:7] WS
[@2,8:8='=',<5>,1:8] ASSIGNMENT_OP
[@3,9:9=' ',<30>,1:9] WS
[@4,10:13='"20"',<27>,1:10] STRING
[@5,15:15='\n',<3>,2:0] NEWLINE
[@6,16:22='assign2',<29>,2:0] VARIABLE
[@7,23:23=' ',<30>,2:7] WS
[@8,24:24='=',<5>,2:8] ASSIGNMENT_OP
[@9,25:25=' ',<30>,2:9] WS
[@10,26:28='123',<25>,2:10] NUMBER
[@11,30:30='\n',<3>,3:0] NEWLINE
[@12,31:37='assign3',<29>,3:0] VARIABLE
[@13,38:38=' ',<30>,3:7] WS
[@14,39:39='=',<5>,3:8] ASSIGNMENT_OP
[@15,40:40=' ',<30>,3:9] WS
[@16,41:44='1.23',<25>,3:10] NUMBER
[@17,46:46='\n',<3>,4:0] NEWLINE
[@18,47:53='assign4',<29>,4:0] VARIABLE
[@19,54:54=' ',<30>,4:7] WS
[@20,55:55='=',<5>,4:8] ASSIGNMENT_OP
[@21,56:56=' ',<30>,4:9] WS
[@22,57:63='assign1',<29>,4:10] VARIABLE
[@23,65:65='\n',<3>,5:0] NEWLINE
[@24,67:67='\n',<3>,6:0] NEWLINE
[@25,68:76='arith_op1',<29>,6:0] VARIABLE
[@26,77:77=' ',<30>,6:9] WS
[@27,78:78='=',<5>,6:10] ASSIGNMENT_OP
[@28,79:79=' ',<30>,6:11] WS
[@29,80:80='1',<25>,6:12] NUMBER
[@30,81:81=' ',<30>,6:13] WS
[@31,82:82='+',<6>,6:14] ARITHMETIC_OP
[@32,83:83=' ',<30>,6:15] WS
[@33,84:84='2',<25>,6:16] NUMBER
[@34,86:86='\n',<3>,7:0] NEWLINE
[@35,87:95='arith_op2',<29>,7:0] VARIABLE
[@36,96:96=' ',<30>,7:9] WS
[@37,97:97='=',<5>,7:10] ASSIGNMENT_OP
[@38,98:98=' ',<30>,7:11] WS
[@39,99:100='13',<25>,7:12] NUMBER
[@40,101:101=' ',<30>,7:14] WS
[@41,102:102='-',<6>,7:15] ARITHMETIC_OP
[@42,103:103=' ',<30>,7:16] WS
[@43,104:104='3',<25>,7:17] NUMBER
[@44,106:106='\n',<3>,8:0] NEWLINE
[@45,107:115='arith_op3',<29>,8:0] VARIABLE
[@46,116:116=' ',<30>,8:9] WS
[@47,117:117='=',<5>,8:10] ASSIGNMENT_OP
[@48,118:118=' ',<30>,8:11] WS
[@49,119:120='10',<25>,8:12] NUMBER
[@50,121:121=' ',<30>,8:14] WS
[@51,122:122='/',<6>,8:15] ARITHMETIC_OP
[@52,123:123=' ',<30>,8:16] WS
[@53,124:132='arith_op1',<29>,8:17] VARIABLE
[@54,134:134='\n',<3>,9:0] NEWLINE
[@55,135:143='arith_op4',<29>,9:0] VARIABLE
[@56,144:144=' ',<30>,9:9] WS
[@57,145:145='=',<5>,9:10] ASSIGNMENT_OP
[@58,146:146=' ',<30>,9:11] WS
[@59,147:149='4.2',<25>,9:12] NUMBER
[@60,150:150=' ',<30>,9:15] WS
[@61,151:151='*',<6>,9:16] ARITHMETIC_OP
[@62,152:152=' ',<30>,9:17] WS
[@63,153:154='10',<25>,9:18] NUMBER
[@64,156:156='\n',<3>,10:0] NEWLINE
[@65,157:165='arith_op5',<29>,10:0] VARIABLE
[@66,166:166=' ',<30>,10:9] WS
[@67,167:167='=',<5>,10:10] ASSIGNMENT_OP
[@68,168:168=' ',<30>,10:11] WS
[@69,169:177='arith_op1',<29>,10:12] VARIABLE
[@70,178:178=' ',<30>,10:21] WS
[@71,179:179='%',<6>,10:22] ARITHMETIC_OP
[@72,180:180=' ',<30>,10:23] WS
[@73,181:189='arith_op2',<29>,10:24] VARIABLE
[@74,191:191='\n',<3>,11:0] NEWLINE
[@75,193:193='\n',<3>,12:0] NEWLINE
[@76,194:202='arith_op1',<29>,12:0] VARIABLE
[@77,203:203=' ',<30>,12:9] WS
[@78,204:205='+=',<5>,12:10] ASSIGNMENT_OP
[@79,206:206=' ',<30>,12:12] WS
[@80,207:215='arith_op2',<29>,12:13] VARIABLE
[@81,217:217='\n',<3>,13:0] NEWLINE
[@82,218:226='arith_op2',<29>,13:0] VARIABLE
[@83,227:227=' ',<30>,13:9] WS
[@84,228:229='-=',<5>,13:10] ASSIGNMENT_OP
[@85,230:230=' ',<30>,13:12] WS
[@86,231:239='arith_op3',<29>,13:13] VARIABLE
[@87,241:241='\n',<3>,14:0] NEWLINE
[@88,242:250='arith_op3',<29>,14:0] VARIABLE
[@89,251:251=' ',<30>,14:9] WS
[@90,252:253='*=',<5>,14:10] ASSIGNMENT_OP
[@91,254:254=' ',<30>,14:12] WS
[@92,255:263='arith_op4',<29>,14:13] VARIABLE
[@93,265:265='\n',<3>,15:0] NEWLINE
[@94,266:274='arith_op4',<29>,15:0] VARIABLE
[@95,275:275=' ',<30>,15:9] WS
[@96,276:277='/=',<5>,15:10] ASSIGNMENT_OP
[@97,278:278=' ',<30>,15:12] WS
[@98,279:287='arith_op5',<29>,15:13] VARIABLE
[@99,289:289='\n',<3>,16:0] NEWLINE
[@100,291:291='\n',<3>,17:0] NEWLINE
[@101,292:297='array1',<29>,17:0] VARIABLE
[@102,298:298=' ',<30>,17:6] WS
[@103,299:299='=',<5>,17:7] ASSIGNMENT_OP
[@104,300:300=' ',<30>,17:8] WS
[@105,301:301='[',<7>,17:9] LBRACKET
[@106,302:302='1',<25>,17:10] NUMBER
[@107,303:303=',',<9>,17:11] COMMA
[@108,304:304=' ',<30>,17:12] WS
[@109,305:305='2',<25>,17:13] NUMBER
[@110,306:306=',',<9>,17:14] COMMA
[@111,307:307=' ',<30>,17:15] WS
[@112,308:308='3',<25>,17:16] NUMBER
[@113,309:309=',',<9>,17:17] COMMA
[@114,310:310=' ',<30>,17:18] WS
[@115,311:311='4',<25>,17:19] NUMBER
[@116,312:312=',',<9>,17:20] COMMA
[@117,313:313=' ',<30>,17:21] WS
[@118,314:314='5',<25>,17:22] NUMBER
[@119,315:315=']',<8>,17:23] RBRACKET
[@120,317:317='\n',<3>,18:0] NEWLINE
[@121,318:323='array2',<29>,18:0] VARIABLE
[@122,324:324=' ',<30>,18:6] WS
[@123,325:325='=',<5>,18:7] ASSIGNMENT_OP
[@124,326:326=' ',<30>,18:8] WS
[@125,327:327='[',<7>,18:9] LBRACKET
[@126,328:330=''a'',<27>,18:10] STRING
[@127,331:331=',',<9>,18:13] COMMA
[@128,332:332=' ',<30>,18:14] WS
[@129,333:335=''b'',<27>,18:15] STRING
[@130,336:336=',',<9>,18:18] COMMA
[@131,337:337=' ',<30>,18:19] WS
[@132,338:340=''c'',<27>,18:20] STRING
[@133,341:341=']',<8>,18:23] RBRACKET
[@134,343:343='\n',<3>,19:0] NEWLINE
[@135,344:349='array3',<29>,19:0] VARIABLE
[@136,350:350=' ',<30>,19:6] WS
[@137,351:351='=',<5>,19:7] ASSIGNMENT_OP
[@138,352:352=' ',<30>,19:8] WS
[@139,353:353='[',<7>,19:9] LBRACKET
[@140,354:356='1.6',<25>,19:10] NUMBER
[@141,357:357=',',<9>,19:13] COMMA
[@142,358:358=' ',<30>,19:14] WS
[@143,359:361='2.7',<25>,19:15] NUMBER
[@144,362:362=',',<9>,19:18] COMMA
[@145,363:363=' ',<30>,19:19] WS
[@146,364:366='3.8',<25>,19:20] NUMBER
[@147,367:367=',',<9>,19:23] COMMA
[@148,368:368=' ',<30>,19:24] WS
[@149,369:371='4.9',<25>,19:25] NUMBER
[@150,372:372=',',<9>,19:28] COMMA
[@151,373:373=' ',<30>,19:29] WS
[@152,374:376='5.0',<25>,19:30] NUMBER
[@153,377:377=']',<8>,19:33] RBRACKET
[@154,379:379='\n',<3>,20:0] NEWLINE
[@155,381:381='\n',<3>,21:0] NEWLINE
[@156,382:385='var1',<29>,21:0] VARIABLE
[@157,386:386=' ',<30>,21:4] WS
[@158,387:387='=',<5>,21:5] ASSIGNMENT_OP
[@159,388:388=' ',<30>,21:6] WS
[@160,389:390='10',<25>,21:7] NUMBER
[@161,392:392='\n',<3>,22:0] NEWLINE
[@162,393:396='var2',<29>,22:0] VARIABLE
[@163,397:397=' ',<30>,22:4] WS
[@164,398:398='=',<5>,22:5] ASSIGNMENT_OP
[@165,399:399=' ',<30>,22:6] WS
[@166,400:403='var1',<29>,22:7] VARIABLE
[@167,404:404='/',<6>,22:11] ARITHMETIC_OP
[@168,405:405='2',<25>,22:12] NUMBER
[@169,406:406=' ',<30>,22:13] WS
[@170,407:407='+',<6>,22:14] ARITHMETIC_OP
[@171,408:408=' ',<30>,22:15] WS
[@172,409:409='5',<25>,22:16] NUMBER
[@173,411:411='\n',<3>,23:0] NEWLINE
[@174,412:415='var3',<29>,23:0] VARIABLE
[@175,416:416=' ',<30>,23:4] WS
[@176,417:417='=',<5>,23:5] ASSIGNMENT_OP
[@177,418:418=' ',<30>,23:6] WS
[@178,419:422='var2',<29>,23:7] VARIABLE
[@179,423:423=' ',<30>,23:11] WS
[@180,424:424='%',<6>,23:12] ARITHMETIC_OP
[@181,425:425=' ',<30>,23:13] WS
[@182,426:426='2',<25>,23:14] NUMBER
[@183,428:428='\n',<3>,24:0] NEWLINE
[@184,429:432='var4',<29>,24:0] VARIABLE
[@185,433:433=' ',<30>,24:4] WS
[@186,434:434='=',<5>,24:5] ASSIGNMENT_OP
[@187,435:435=' ',<30>,24:6] WS
[@188,436:436='1',<25>,24:7] NUMBER
[@189,438:438='\n',<3>,25:0] NEWLINE
[@190,440:440='\n',<3>,26:0] NEWLINE
[@191,441:444='flag',<29>,26:0] VARIABLE
[@192,445:445=' ',<30>,26:4] WS
[@193,446:446='=',<5>,26:5] ASSIGNMENT_OP
[@194,447:447=' ',<30>,26:6] WS
[@195,448:451='True',<26>,26:7] BOOLEAN
[@196,451:451='e',<3>,26:11] NEWLINE
[@197,451:451='<DEDENT>',<2>,26:11] DEDENT
[@198,447:451=' True',<-1>,26:11] WS_SKIPPED
Parse tree:
(stat 
   (expr 
      (first_block 
         (line 
            (assignment assign1   
               (assignment_operator =)   
               (expression 
                  (value "20")))) \n 
         (line 
            (assignment assign2   
               (assignment_operator =)   
               (expression 
                  (value 123)))) \n 
         (line 
            (assignment assign3   
               (assignment_operator =)   
               (expression 
                  (value 1.23)))) \n 
         (line 
            (assignment assign4   
               (assignment_operator =)   
               (expression 
                  (value assign1)))) \n \n 
         (line 
            (assignment arith_op1   
               (assignment_operator =)   
               (expression 
                  (value 1)   
                  (operator +)   
                  (value 2)))) \n 
         (line 
            (assignment arith_op2   
               (assignment_operator =)   
               (expression 
                  (value 13)   
                  (operator -)   
                  (value 3)))) \n 
         (line 
            (assignment arith_op3   
               (assignment_operator =)   
               (expression 
                  (value 10)   
                  (operator /)   
                  (value arith_op1)))) \n 
         (line 
            (assignment arith_op4   
               (assignment_operator =)   
               (expression 
                  (value 4.2)   
                  (operator *)   
                  (value 10)))) \n 
         (line 
            (assignment arith_op5   
               (assignment_operator =)   
               (expression 
                  (value arith_op1)   
                  (operator %)   
                  (value arith_op2)))) \n \n 
         (line 
            (assignment arith_op1   
               (assignment_operator +=)   
               (expression 
                  (value arith_op2)))) \n 
         (line 
            (assignment arith_op2   
               (assignment_operator -=)   
               (expression 
                  (value arith_op3)))) \n 
         (line 
            (assignment arith_op3   
               (assignment_operator *=)   
               (expression 
                  (value arith_op4)))) \n 
         (line 
            (assignment arith_op4   
               (assignment_operator /=)   
               (expression 
                  (value arith_op5)))) \n \n 
         (line 
            (assignment array1   
               (assignment_operator =)   
               (expression 
                  (value 
                     (array [ 
                        (value 1) ,   
                        (value 2) ,   
                        (value 3) ,   
                        (value 4) ,   
                        (value 5) ]))))) \n 
         (line 
            (assignment array2   
               (assignment_operator =)   
               (expression 
                  (value 
                     (array [ 
                        (value 'a') ,   
                        (value 'b') ,   
                        (value 'c') ]))))) \n 
         (line 
            (assignment array3   
               (assignment_operator =)   
               (expression 
                  (value 
                     (array [ 
                        (value 1.6) ,   
                        (value 2.7) ,   
                        (value 3.8) ,   
                        (value 4.9) ,   
                        (value 5.0) ]))))) \n \n 
         (line 
            (assignment var1   
               (assignment_operator =)   
               (expression 
                  (value 10)))) \n 
         (line 
            (assignment var2   
               (assignment_operator =)   
               (expression 
                  (value var1) 
                  (operator /) 
                  (value 2)   
                  (operator +)   
                  (value 5)))) \n 
         (line 
            (assignment var3   
               (assignment_operator =)   
               (expression 
                  (value var2)   
                  (operator %)   
                  (value 2)))) \n 
         (line 
            (assignment var4   
               (assignment_operator =)   
               (expression 
                  (value 1)))) \n \n 
         (line 
            (assignment flag   
               (assignment_operator =)   
               (expression 
                  (value True)))) e) <DEDENT>  True))

Project Deliverable 1: Passed
```