> Can't generate an image of the tree due to indentation implementation\
> Token list and parse tree as text below

```
(popl) $ python ./scripts/combine_grammars.py && antlr4 -Dlanguage=Python3 ./grammars/FullLexer.g4 ./grammars/FullParser.g4 && python main.py
Generated grammar files. Compile with:
antlr4 -Dlanguage=Python3 ./grammars/FullLexer.g4 ./grammars/FullParser.g4
Tokenizing ./final_tests/project_deliverable_2.py:
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
[@196,453:453='\n',<3>,27:0] NEWLINE
[@197,455:455='\n',<3>,28:0] NEWLINE
[@198,456:462='assign1',<29>,28:0] VARIABLE
[@199,463:463=' ',<30>,28:7] WS
[@200,464:464='=',<5>,28:8] ASSIGNMENT_OP
[@201,465:465=' ',<30>,28:9] WS
[@202,466:467='""',<27>,28:10] STRING
[@203,469:469='\n',<3>,29:0] NEWLINE
[@204,471:471='\n',<3>,30:0] NEWLINE
[@205,472:473='if',<10>,30:0] IF
[@206,474:474=' ',<30>,30:2] WS
[@207,475:478='var1',<29>,30:3] VARIABLE
[@208,479:479=' ',<30>,30:7] WS
[@209,480:480='>',<16>,30:8] COMPARISON_OP
[@210,481:481=' ',<30>,30:9] WS
[@211,482:485='var2',<29>,30:10] VARIABLE
[@212,486:486=':',<13>,30:14] COLON
[@213,489:489='\t',<3>,31:1] NEWLINE
[@214,489:489='<INDENT>',<1>,30:1] INDENT
[@215,490:498='arith_op1',<29>,31:1] VARIABLE
[@216,499:499=' ',<30>,31:10] WS
[@217,500:500='=',<5>,31:11] ASSIGNMENT_OP
[@218,501:501=' ',<30>,31:12] WS
[@219,502:502='1',<25>,31:13] NUMBER
[@220,503:503=' ',<30>,31:14] WS
[@221,504:504='+',<6>,31:15] ARITHMETIC_OP
[@222,505:505=' ',<30>,31:16] WS
[@223,506:506='2',<25>,31:17] NUMBER
[@224,509:509='\t',<3>,32:1] NEWLINE
[@225,510:516='assign1',<29>,32:1] VARIABLE
[@226,517:517=' ',<30>,32:8] WS
[@227,518:518='=',<5>,32:9] ASSIGNMENT_OP
[@228,519:519=' ',<30>,32:10] WS
[@229,520:530='"text data"',<27>,32:11] STRING
[@230,532:532='\n',<3>,33:0] NEWLINE
[@231,532:532='<DEDENT>',<2>,32:0] DEDENT
[@232,534:534='\n',<3>,34:0] NEWLINE
[@233,535:536='if',<10>,34:0] IF
[@234,537:537=' ',<30>,34:2] WS
[@235,538:541='var1',<29>,34:3] VARIABLE
[@236,542:542=' ',<30>,34:7] WS
[@237,543:544='<=',<16>,34:8] COMPARISON_OP
[@238,545:545=' ',<30>,34:10] WS
[@239,546:549='var2',<29>,34:11] VARIABLE
[@240,550:550=' ',<30>,34:15] WS
[@241,551:553='and',<17>,34:16] LOGICAL_OP
[@242,554:554=' ',<30>,34:19] WS
[@243,555:558='var3',<29>,34:20] VARIABLE
[@244,559:559=' ',<30>,34:24] WS
[@245,560:561='==',<16>,34:25] COMPARISON_OP
[@246,562:562=' ',<30>,34:27] WS
[@247,563:566='var4',<29>,34:28] VARIABLE
[@248,567:567=':',<13>,34:32] COLON
[@249,570:570='\t',<3>,35:1] NEWLINE
[@250,570:570='<INDENT>',<1>,34:1] INDENT
[@251,571:579='arith_op1',<29>,35:1] VARIABLE
[@252,580:580=' ',<30>,35:10] WS
[@253,581:581='=',<5>,35:11] ASSIGNMENT_OP
[@254,582:582=' ',<30>,35:12] WS
[@255,583:583='1',<25>,35:13] NUMBER
[@256,584:584=' ',<30>,35:14] WS
[@257,585:585='+',<6>,35:15] ARITHMETIC_OP
[@258,586:586=' ',<30>,35:16] WS
[@259,587:587='2',<25>,35:17] NUMBER
[@260,590:590='\t',<3>,36:1] NEWLINE
[@261,591:597='assign1',<29>,36:1] VARIABLE
[@262,598:598=' ',<30>,36:8] WS
[@263,599:599='=',<5>,36:9] ASSIGNMENT_OP
[@264,600:600=' ',<30>,36:10] WS
[@265,601:611='"text data"',<27>,36:11] STRING
[@266,613:613='\n',<3>,37:0] NEWLINE
[@267,613:613='<DEDENT>',<2>,36:0] DEDENT
[@268,614:617='else',<12>,37:0] ELSE
[@269,618:618=':',<13>,37:4] COLON
[@270,621:621='\t',<3>,38:1] NEWLINE
[@271,621:621='<INDENT>',<1>,37:1] INDENT
[@272,622:630='arith_op4',<29>,38:1] VARIABLE
[@273,631:631=' ',<30>,38:10] WS
[@274,632:632='=',<5>,38:11] ASSIGNMENT_OP
[@275,633:633=' ',<30>,38:12] WS
[@276,634:636='4.2',<25>,38:13] NUMBER
[@277,637:637=' ',<30>,38:16] WS
[@278,638:638='*',<6>,38:17] ARITHMETIC_OP
[@279,639:639=' ',<30>,38:18] WS
[@280,640:641='10',<25>,38:19] NUMBER
[@281,644:644='\t',<3>,39:1] NEWLINE
[@282,645:653='arith_op3',<29>,39:1] VARIABLE
[@283,654:654=' ',<30>,39:10] WS
[@284,655:656='*=',<5>,39:11] ASSIGNMENT_OP
[@285,657:657=' ',<30>,39:13] WS
[@286,658:666='arith_op4',<29>,39:14] VARIABLE
[@287,669:669='\t',<3>,40:1] NEWLINE
[@288,671:671='\n',<3>,41:0] NEWLINE
[@289,671:671='<DEDENT>',<2>,39:0] DEDENT
[@290,672:675='data',<29>,41:0] VARIABLE
[@291,676:676=' ',<30>,41:4] WS
[@292,677:677='=',<5>,41:5] ASSIGNMENT_OP
[@293,678:678=' ',<30>,41:6] WS
[@294,679:679='0',<25>,41:7] NUMBER
[@295,681:681='\n',<3>,42:0] NEWLINE
[@296,683:683='\n',<3>,43:0] NEWLINE
[@297,684:685='if',<10>,43:0] IF
[@298,686:686=' ',<30>,43:2] WS
[@299,687:690='var1',<29>,43:3] VARIABLE
[@300,691:691=' ',<30>,43:7] WS
[@301,692:693='!=',<16>,43:8] COMPARISON_OP
[@302,694:694=' ',<30>,43:10] WS
[@303,695:698='var2',<29>,43:11] VARIABLE
[@304,699:699=' ',<30>,43:15] WS
[@305,700:701='or',<17>,43:16] LOGICAL_OP
[@306,702:702=' ',<30>,43:18] WS
[@307,703:706='var3',<29>,43:19] VARIABLE
[@308,707:707=' ',<30>,43:23] WS
[@309,708:709='>=',<16>,43:24] COMPARISON_OP
[@310,710:710=' ',<30>,43:26] WS
[@311,711:714='var4',<29>,43:27] VARIABLE
[@312,715:715=':',<13>,43:31] COLON
[@313,718:718='\t',<3>,44:1] NEWLINE
[@314,718:718='<INDENT>',<1>,43:1] INDENT
[@315,719:722='flag',<29>,44:1] VARIABLE
[@316,723:723=' ',<30>,44:5] WS
[@317,724:724='=',<5>,44:6] ASSIGNMENT_OP
[@318,725:725=' ',<30>,44:7] WS
[@319,726:729='True',<26>,44:8] BOOLEAN
[@320,731:731='\n',<3>,45:0] NEWLINE
[@321,731:731='<DEDENT>',<2>,44:0] DEDENT
[@322,732:735='elif',<11>,45:0] ELIF
[@323,736:736=' ',<30>,45:4] WS
[@324,737:737='(',<14>,45:5] LPAREN
[@325,738:740='not',<18>,45:6] NOT_OP
[@326,741:741=' ',<30>,45:9] WS
[@327,742:745='flag',<29>,45:10] VARIABLE
[@328,746:746=')',<15>,45:14] RPAREN
[@329,747:747=' ',<30>,45:15] WS
[@330,748:749='>=',<16>,45:16] COMPARISON_OP
[@331,750:750=' ',<30>,45:18] WS
[@332,751:751='(',<14>,45:19] LPAREN
[@333,752:755='var3',<29>,45:20] VARIABLE
[@334,756:756=' ',<30>,45:24] WS
[@335,757:757='>',<16>,45:25] COMPARISON_OP
[@336,758:758=' ',<30>,45:26] WS
[@337,759:760='10',<25>,45:27] NUMBER
[@338,761:761=')',<15>,45:29] RPAREN
[@339,762:762=':',<13>,45:30] COLON
[@340,765:765='\t',<3>,46:1] NEWLINE
[@341,765:765='<INDENT>',<1>,45:1] INDENT
[@342,766:769='flag',<29>,46:1] VARIABLE
[@343,770:770=' ',<30>,46:5] WS
[@344,771:771='=',<5>,46:6] ASSIGNMENT_OP
[@345,772:772=' ',<30>,46:7] WS
[@346,773:777='False',<26>,46:8] BOOLEAN
[@347,779:779='\n',<3>,47:0] NEWLINE
[@348,779:779='<DEDENT>',<2>,46:0] DEDENT
[@349,780:783='else',<12>,47:0] ELSE
[@350,784:784=':',<13>,47:4] COLON
[@351,787:787='\t',<3>,48:1] NEWLINE
[@352,787:787='<INDENT>',<1>,47:1] INDENT
[@353,788:791='data',<29>,48:1] VARIABLE
[@354,792:792=' ',<30>,48:5] WS
[@355,793:793='=',<5>,48:6] ASSIGNMENT_OP
[@356,794:794=' ',<30>,48:7] WS
[@357,795:796='-1',<25>,48:8] NUMBER
[@358,796:796='1',<3>,48:10] NEWLINE
[@359,796:796='<DEDENT>',<2>,48:10] DEDENT
[@360,796:796='<DEDENT>',<2>,48:10] DEDENT
[@361,792:796=' = -1',<-1>,48:10] WS_SKIPPED
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
                  (value True)))) \n \n 
         (line 
            (assignment assign1   
               (assignment_operator =)   
               (expression 
                  (value "")))) \n \n 
         (line 
            (if_block if   
               (condition 
                  (comparison_condition 
                     (value var1))   >   
                  (comparison_condition 
                     (value var2))) : \t 
               (block <INDENT> 
                  (first_block 
                     (line 
                        (assignment arith_op1   
                           (assignment_operator =)   
                           (expression 
                              (value 1)   
                              (operator +)   
                              (value 2)))) \t 
                     (line 
                        (assignment assign1   
                           (assignment_operator =)   
                           (expression 
                              (value "text data")))) \n) <DEDENT>))) \n 
         (line 
            (if_block if   
               (condition 
                  (comparison_condition 
                     (value var1))   <=   
                  (comparison_condition 
                     (value var2))   and   
                  (comparison_condition 
                     (value var3))   ==   
                  (comparison_condition 
                     (value var4))) : \t 
               (block <INDENT> 
                  (first_block 
                     (line 
                        (assignment arith_op1   
                           (assignment_operator =)   
                           (expression 
                              (value 1)   
                              (operator +)   
                              (value 2)))) \t 
                     (line 
                        (assignment assign1   
                           (assignment_operator =)   
                           (expression 
                              (value "text data")))) \n) <DEDENT>) 
               (else_block else : \t 
                  (block <INDENT> 
                     (first_block 
                        (line 
                           (assignment arith_op4   
                              (assignment_operator =)   
                              (expression 
                                 (value 4.2)   
                                 (operator *)   
                                 (value 10)))) \t 
                        (line 
                           (assignment arith_op3   
                              (assignment_operator *=)   
                              (expression 
                                 (value arith_op4)))) \t \n) <DEDENT>)))) 
         (line 
            (assignment data   
               (assignment_operator =)   
               (expression 
                  (value 0)))) \n \n 
         (line 
            (if_block if   
               (condition 
                  (comparison_condition 
                     (value var1))   !=   
                  (comparison_condition 
                     (value var2))   or   
                  (comparison_condition 
                     (value var3))   >=   
                  (comparison_condition 
                     (value var4))) : \t 
               (block <INDENT> 
                  (first_block 
                     (line 
                        (assignment flag   
                           (assignment_operator =)   
                           (expression 
                              (value True)))) \n) <DEDENT>) 
               (elif_block elif 
                  (condition   
                     (comparison_condition ( 
                        (condition 
                           (comparison_condition not   
                              (comparison_condition 
                                 (value flag)))) ))   >=   
                  (comparison_condition ( 
                     (condition 
                        (comparison_condition 
                           (value var3))   >   
                        (comparison_condition 
                           (value 10))) ))) : \t 
            (block <INDENT> 
               (first_block 
                  (line 
                     (assignment flag   
                        (assignment_operator =)   
                        (expression 
                           (value False)))) \n) <DEDENT>)) 
         (else_block else : \t 
            (block <INDENT> 
               (first_block 
                  (line 
                     (assignment data   
                        (assignment_operator =)   
                        (expression 
                           (value -1)))) 1) <DEDENT>))))) <DEDENT>  = -1))

Project Deliverable 2: Passed
```