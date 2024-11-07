> Can't generate an image of the tree due to indentation implementation\
> Token list and parse tree as text below

```
(popl) $ python ./scripts/combine_grammars.py && antlr4 -Dlanguage=Python3 ./grammars/FullLexer.g4 ./grammars/FullParser.g4 && python main.py
Generated grammar files. Compile with:
antlr4 -Dlanguage=Python3 ./grammars/FullLexer.g4 ./grammars/FullParser.g4
Tokenizing ./final_tests/project_deliverable_3.py:
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
[@55,135:149='# Deliverable 1',<23>,9:0] SINGLE_LINE_COMMENT
[@56,151:151='\n',<3>,10:0] NEWLINE
[@57,152:160='arith_op4',<29>,10:0] VARIABLE
[@58,161:161=' ',<30>,10:9] WS
[@59,162:162='=',<5>,10:10] ASSIGNMENT_OP
[@60,163:163=' ',<30>,10:11] WS
[@61,164:166='4.2',<25>,10:12] NUMBER
[@62,167:167=' ',<30>,10:15] WS
[@63,168:168='*',<6>,10:16] ARITHMETIC_OP
[@64,169:169=' ',<30>,10:17] WS
[@65,170:171='10',<25>,10:18] NUMBER
[@66,173:173='\n',<3>,11:0] NEWLINE
[@67,174:182='arith_op5',<29>,11:0] VARIABLE
[@68,183:183=' ',<30>,11:9] WS
[@69,184:184='=',<5>,11:10] ASSIGNMENT_OP
[@70,185:185=' ',<30>,11:11] WS
[@71,186:194='arith_op1',<29>,11:12] VARIABLE
[@72,195:195=' ',<30>,11:21] WS
[@73,196:196='%',<6>,11:22] ARITHMETIC_OP
[@74,197:197=' ',<30>,11:23] WS
[@75,198:206='arith_op2',<29>,11:24] VARIABLE
[@76,208:208='\n',<3>,12:0] NEWLINE
[@77,210:210='\n',<3>,13:0] NEWLINE
[@78,211:219='arith_op1',<29>,13:0] VARIABLE
[@79,220:220=' ',<30>,13:9] WS
[@80,221:222='+=',<5>,13:10] ASSIGNMENT_OP
[@81,223:223=' ',<30>,13:12] WS
[@82,224:232='arith_op2',<29>,13:13] VARIABLE
[@83,234:234='\n',<3>,14:0] NEWLINE
[@84,235:243='arith_op2',<29>,14:0] VARIABLE
[@85,244:244=' ',<30>,14:9] WS
[@86,245:246='-=',<5>,14:10] ASSIGNMENT_OP
[@87,247:247=' ',<30>,14:12] WS
[@88,248:256='arith_op3',<29>,14:13] VARIABLE
[@89,258:258='\n',<3>,15:0] NEWLINE
[@90,259:267='arith_op3',<29>,15:0] VARIABLE
[@91,268:268=' ',<30>,15:9] WS
[@92,269:270='*=',<5>,15:10] ASSIGNMENT_OP
[@93,271:271=' ',<30>,15:12] WS
[@94,272:280='arith_op4',<29>,15:13] VARIABLE
[@95,282:282='\n',<3>,16:0] NEWLINE
[@96,283:291='arith_op4',<29>,16:0] VARIABLE
[@97,292:292=' ',<30>,16:9] WS
[@98,293:294='/=',<5>,16:10] ASSIGNMENT_OP
[@99,295:295=' ',<30>,16:12] WS
[@100,296:304='arith_op5',<29>,16:13] VARIABLE
[@101,306:306='\n',<3>,17:0] NEWLINE
[@102,308:308='\n',<3>,18:0] NEWLINE
[@103,309:314='array1',<29>,18:0] VARIABLE
[@104,315:315=' ',<30>,18:6] WS
[@105,316:316='=',<5>,18:7] ASSIGNMENT_OP
[@106,317:317=' ',<30>,18:8] WS
[@107,318:318='[',<7>,18:9] LBRACKET
[@108,319:319='1',<25>,18:10] NUMBER
[@109,320:320=',',<9>,18:11] COMMA
[@110,321:321=' ',<30>,18:12] WS
[@111,322:322='2',<25>,18:13] NUMBER
[@112,323:323=',',<9>,18:14] COMMA
[@113,324:324=' ',<30>,18:15] WS
[@114,325:325='3',<25>,18:16] NUMBER
[@115,326:326=',',<9>,18:17] COMMA
[@116,327:327=' ',<30>,18:18] WS
[@117,328:328='4',<25>,18:19] NUMBER
[@118,329:329=',',<9>,18:20] COMMA
[@119,330:330=' ',<30>,18:21] WS
[@120,331:331='5',<25>,18:22] NUMBER
[@121,332:332=']',<8>,18:23] RBRACKET
[@122,334:334='\n',<3>,19:0] NEWLINE
[@123,335:340='array2',<29>,19:0] VARIABLE
[@124,341:341=' ',<30>,19:6] WS
[@125,342:342='=',<5>,19:7] ASSIGNMENT_OP
[@126,343:343=' ',<30>,19:8] WS
[@127,344:344='[',<7>,19:9] LBRACKET
[@128,345:347=''a'',<27>,19:10] STRING
[@129,348:348=',',<9>,19:13] COMMA
[@130,349:349=' ',<30>,19:14] WS
[@131,350:352=''b'',<27>,19:15] STRING
[@132,353:353=',',<9>,19:18] COMMA
[@133,354:354=' ',<30>,19:19] WS
[@134,355:357=''c'',<27>,19:20] STRING
[@135,358:358=']',<8>,19:23] RBRACKET
[@136,360:360='\n',<3>,20:0] NEWLINE
[@137,361:366='array3',<29>,20:0] VARIABLE
[@138,367:367=' ',<30>,20:6] WS
[@139,368:368='=',<5>,20:7] ASSIGNMENT_OP
[@140,369:369=' ',<30>,20:8] WS
[@141,370:370='[',<7>,20:9] LBRACKET
[@142,371:373='1.6',<25>,20:10] NUMBER
[@143,374:374=',',<9>,20:13] COMMA
[@144,375:375=' ',<30>,20:14] WS
[@145,376:378='2.7',<25>,20:15] NUMBER
[@146,379:379=',',<9>,20:18] COMMA
[@147,380:380=' ',<30>,20:19] WS
[@148,381:383='3.8',<25>,20:20] NUMBER
[@149,384:384=',',<9>,20:23] COMMA
[@150,385:385=' ',<30>,20:24] WS
[@151,386:388='4.9',<25>,20:25] NUMBER
[@152,389:389=',',<9>,20:28] COMMA
[@153,390:390=' ',<30>,20:29] WS
[@154,391:393='5.0',<25>,20:30] NUMBER
[@155,394:394=']',<8>,20:33] RBRACKET
[@156,396:396='\n',<3>,21:0] NEWLINE
[@157,398:398='\n',<3>,22:0] NEWLINE
[@158,399:402='var1',<29>,22:0] VARIABLE
[@159,403:403=' ',<30>,22:4] WS
[@160,404:404='=',<5>,22:5] ASSIGNMENT_OP
[@161,405:405=' ',<30>,22:6] WS
[@162,406:407='10',<25>,22:7] NUMBER
[@163,409:409='\n',<3>,23:0] NEWLINE
[@164,410:413='var2',<29>,23:0] VARIABLE
[@165,414:414=' ',<30>,23:4] WS
[@166,415:415='=',<5>,23:5] ASSIGNMENT_OP
[@167,416:416=' ',<30>,23:6] WS
[@168,417:420='var1',<29>,23:7] VARIABLE
[@169,421:421='/',<6>,23:11] ARITHMETIC_OP
[@170,422:422='2',<25>,23:12] NUMBER
[@171,423:423=' ',<30>,23:13] WS
[@172,424:424='+',<6>,23:14] ARITHMETIC_OP
[@173,425:425=' ',<30>,23:15] WS
[@174,426:426='5',<25>,23:16] NUMBER
[@175,428:428='\n',<3>,24:0] NEWLINE
[@176,429:432='var3',<29>,24:0] VARIABLE
[@177,433:433=' ',<30>,24:4] WS
[@178,434:434='=',<5>,24:5] ASSIGNMENT_OP
[@179,435:435=' ',<30>,24:6] WS
[@180,436:439='var2',<29>,24:7] VARIABLE
[@181,440:440=' ',<30>,24:11] WS
[@182,441:441='%',<6>,24:12] ARITHMETIC_OP
[@183,442:442=' ',<30>,24:13] WS
[@184,443:443='2',<25>,24:14] NUMBER
[@185,445:445='\n',<3>,25:0] NEWLINE
[@186,446:449='var4',<29>,25:0] VARIABLE
[@187,450:450=' ',<30>,25:4] WS
[@188,451:451='=',<5>,25:5] ASSIGNMENT_OP
[@189,452:452=' ',<30>,25:6] WS
[@190,453:453='1',<25>,25:7] NUMBER
[@191,455:455='\n',<3>,26:0] NEWLINE
[@192,457:457='\n',<3>,27:0] NEWLINE
[@193,458:461='flag',<29>,27:0] VARIABLE
[@194,462:462=' ',<30>,27:4] WS
[@195,463:463='=',<5>,27:5] ASSIGNMENT_OP
[@196,464:464=' ',<30>,27:6] WS
[@197,465:468='True',<26>,27:7] BOOLEAN
[@198,470:470='\n',<3>,28:0] NEWLINE
[@199,472:472='\n',<3>,29:0] NEWLINE
[@200,473:479='assign1',<29>,29:0] VARIABLE
[@201,480:480=' ',<30>,29:7] WS
[@202,481:481='=',<5>,29:8] ASSIGNMENT_OP
[@203,482:482=' ',<30>,29:9] WS
[@204,483:484='""',<27>,29:10] STRING
[@205,486:486='\n',<3>,30:0] NEWLINE
[@206,488:488='\n',<3>,31:0] NEWLINE
[@207,489:503='# Deliverable 2',<23>,31:0] SINGLE_LINE_COMMENT
[@208,505:505='\n',<3>,32:0] NEWLINE
[@209,507:507='\n',<3>,33:0] NEWLINE
[@210,508:509='if',<10>,33:0] IF
[@211,510:510=' ',<30>,33:2] WS
[@212,511:514='var1',<29>,33:3] VARIABLE
[@213,515:515=' ',<30>,33:7] WS
[@214,516:516='>',<16>,33:8] COMPARISON_OP
[@215,517:517=' ',<30>,33:9] WS
[@216,518:521='var2',<29>,33:10] VARIABLE
[@217,522:522=':',<13>,33:14] COLON
[@218,525:525='\t',<3>,34:1] NEWLINE
[@219,525:525='<INDENT>',<1>,33:1] INDENT
[@220,526:534='arith_op1',<29>,34:1] VARIABLE
[@221,535:535=' ',<30>,34:10] WS
[@222,536:536='=',<5>,34:11] ASSIGNMENT_OP
[@223,537:537=' ',<30>,34:12] WS
[@224,538:538='1',<25>,34:13] NUMBER
[@225,539:539=' ',<30>,34:14] WS
[@226,540:540='+',<6>,34:15] ARITHMETIC_OP
[@227,541:541=' ',<30>,34:16] WS
[@228,542:542='2',<25>,34:17] NUMBER
[@229,545:545='\t',<3>,35:1] NEWLINE
[@230,546:552='assign1',<29>,35:1] VARIABLE
[@231,553:553=' ',<30>,35:8] WS
[@232,554:554='=',<5>,35:9] ASSIGNMENT_OP
[@233,555:555=' ',<30>,35:10] WS
[@234,556:566='"text data"',<27>,35:11] STRING
[@235,568:568='\n',<3>,36:0] NEWLINE
[@236,568:568='<DEDENT>',<2>,35:0] DEDENT
[@237,570:570='\n',<3>,37:0] NEWLINE
[@238,571:572='if',<10>,37:0] IF
[@239,573:573=' ',<30>,37:2] WS
[@240,574:577='var1',<29>,37:3] VARIABLE
[@241,578:578=' ',<30>,37:7] WS
[@242,579:580='<=',<16>,37:8] COMPARISON_OP
[@243,581:581=' ',<30>,37:10] WS
[@244,582:585='var2',<29>,37:11] VARIABLE
[@245,586:586=' ',<30>,37:15] WS
[@246,587:589='and',<17>,37:16] LOGICAL_OP
[@247,590:590=' ',<30>,37:19] WS
[@248,591:594='var3',<29>,37:20] VARIABLE
[@249,595:595=' ',<30>,37:24] WS
[@250,596:597='==',<16>,37:25] COMPARISON_OP
[@251,598:598=' ',<30>,37:27] WS
[@252,599:602='var4',<29>,37:28] VARIABLE
[@253,603:603=':',<13>,37:32] COLON
[@254,606:606='\t',<3>,38:1] NEWLINE
[@255,606:606='<INDENT>',<1>,37:1] INDENT
[@256,607:615='arith_op1',<29>,38:1] VARIABLE
[@257,616:616=' ',<30>,38:10] WS
[@258,617:617='=',<5>,38:11] ASSIGNMENT_OP
[@259,618:618=' ',<30>,38:12] WS
[@260,619:619='1',<25>,38:13] NUMBER
[@261,620:620=' ',<30>,38:14] WS
[@262,621:621='+',<6>,38:15] ARITHMETIC_OP
[@263,622:622=' ',<30>,38:16] WS
[@264,623:623='2',<25>,38:17] NUMBER
[@265,626:626='\t',<3>,39:1] NEWLINE
[@266,627:633='assign1',<29>,39:1] VARIABLE
[@267,634:634=' ',<30>,39:8] WS
[@268,635:635='=',<5>,39:9] ASSIGNMENT_OP
[@269,636:636=' ',<30>,39:10] WS
[@270,637:647='"text data"',<27>,39:11] STRING
[@271,649:649='\n',<3>,40:0] NEWLINE
[@272,649:649='<DEDENT>',<2>,39:0] DEDENT
[@273,650:653='else',<12>,40:0] ELSE
[@274,654:654=':',<13>,40:4] COLON
[@275,657:657='\t',<3>,41:1] NEWLINE
[@276,657:657='<INDENT>',<1>,40:1] INDENT
[@277,658:666='arith_op4',<29>,41:1] VARIABLE
[@278,667:667=' ',<30>,41:10] WS
[@279,668:668='=',<5>,41:11] ASSIGNMENT_OP
[@280,669:669=' ',<30>,41:12] WS
[@281,670:672='4.2',<25>,41:13] NUMBER
[@282,673:673=' ',<30>,41:16] WS
[@283,674:674='*',<6>,41:17] ARITHMETIC_OP
[@284,675:675=' ',<30>,41:18] WS
[@285,676:677='10',<25>,41:19] NUMBER
[@286,680:680='\t',<3>,42:1] NEWLINE
[@287,681:689='arith_op3',<29>,42:1] VARIABLE
[@288,690:690=' ',<30>,42:10] WS
[@289,691:692='*=',<5>,42:11] ASSIGNMENT_OP
[@290,693:693=' ',<30>,42:13] WS
[@291,694:702='arith_op4',<29>,42:14] VARIABLE
[@292,705:705='\t',<3>,43:1] NEWLINE
[@293,707:707='\n',<3>,44:0] NEWLINE
[@294,707:707='<DEDENT>',<2>,42:0] DEDENT
[@295,708:711='data',<29>,44:0] VARIABLE
[@296,712:712=' ',<30>,44:4] WS
[@297,713:713='=',<5>,44:5] ASSIGNMENT_OP
[@298,714:714=' ',<30>,44:6] WS
[@299,715:715='0',<25>,44:7] NUMBER
[@300,717:717='\n',<3>,45:0] NEWLINE
[@301,719:719='\n',<3>,46:0] NEWLINE
[@302,720:721='if',<10>,46:0] IF
[@303,722:722=' ',<30>,46:2] WS
[@304,723:726='var1',<29>,46:3] VARIABLE
[@305,727:727=' ',<30>,46:7] WS
[@306,728:729='!=',<16>,46:8] COMPARISON_OP
[@307,730:730=' ',<30>,46:10] WS
[@308,731:734='var2',<29>,46:11] VARIABLE
[@309,735:735=' ',<30>,46:15] WS
[@310,736:737='or',<17>,46:16] LOGICAL_OP
[@311,738:738=' ',<30>,46:18] WS
[@312,739:742='var3',<29>,46:19] VARIABLE
[@313,743:743=' ',<30>,46:23] WS
[@314,744:745='>=',<16>,46:24] COMPARISON_OP
[@315,746:746=' ',<30>,46:26] WS
[@316,747:750='var4',<29>,46:27] VARIABLE
[@317,751:751=':',<13>,46:31] COLON
[@318,754:754='\t',<3>,47:1] NEWLINE
[@319,754:754='<INDENT>',<1>,46:1] INDENT
[@320,755:758='flag',<29>,47:1] VARIABLE
[@321,759:759=' ',<30>,47:5] WS
[@322,760:760='=',<5>,47:6] ASSIGNMENT_OP
[@323,761:761=' ',<30>,47:7] WS
[@324,762:765='True',<26>,47:8] BOOLEAN
[@325,767:767='\n',<3>,48:0] NEWLINE
[@326,767:767='<DEDENT>',<2>,47:0] DEDENT
[@327,768:771='elif',<11>,48:0] ELIF
[@328,772:772=' ',<30>,48:4] WS
[@329,773:773='(',<14>,48:5] LPAREN
[@330,774:776='not',<18>,48:6] NOT_OP
[@331,777:777=' ',<30>,48:9] WS
[@332,778:781='flag',<29>,48:10] VARIABLE
[@333,782:782=')',<15>,48:14] RPAREN
[@334,783:783=' ',<30>,48:15] WS
[@335,784:786='and',<17>,48:16] LOGICAL_OP
[@336,787:787=' ',<30>,48:19] WS
[@337,788:791='var3',<29>,48:20] VARIABLE
[@338,792:792=' ',<30>,48:24] WS
[@339,793:793='>',<16>,48:25] COMPARISON_OP
[@340,794:794=' ',<30>,48:26] WS
[@341,795:796='10',<25>,48:27] NUMBER
[@342,797:797=':',<13>,48:29] COLON
[@343,800:800='\t',<3>,49:1] NEWLINE
[@344,800:800='<INDENT>',<1>,48:1] INDENT
[@345,801:804='flag',<29>,49:1] VARIABLE
[@346,805:805=' ',<30>,49:5] WS
[@347,806:806='=',<5>,49:6] ASSIGNMENT_OP
[@348,807:807=' ',<30>,49:7] WS
[@349,808:812='False',<26>,49:8] BOOLEAN
[@350,814:814='\n',<3>,50:0] NEWLINE
[@351,814:814='<DEDENT>',<2>,49:0] DEDENT
[@352,815:818='else',<12>,50:0] ELSE
[@353,819:819=':',<13>,50:4] COLON
[@354,822:822='\t',<3>,51:1] NEWLINE
[@355,822:822='<INDENT>',<1>,50:1] INDENT
[@356,823:826='data',<29>,51:1] VARIABLE
[@357,827:827=' ',<30>,51:5] WS
[@358,828:828='=',<5>,51:6] ASSIGNMENT_OP
[@359,829:829=' ',<30>,51:7] WS
[@360,830:831='-1',<25>,51:8] NUMBER
[@361,833:833='\n',<3>,52:0] NEWLINE
[@362,833:833='<DEDENT>',<2>,51:0] DEDENT
[@363,835:835='\n',<3>,53:0] NEWLINE
[@364,836:850='# Deliverable 3',<23>,53:0] SINGLE_LINE_COMMENT
[@365,852:852='\n',<3>,54:0] NEWLINE
[@366,854:854='\n',<3>,55:0] NEWLINE
[@367,855:871='## comment test 1',<23>,55:0] SINGLE_LINE_COMMENT
[@368,873:873='\n',<3>,56:0] NEWLINE
[@369,875:875='\n',<3>,57:0] NEWLINE
[@370,876:938='''' \r\n\tcomment test 2\r\n\tadding more comments\r\n\tand more...\r\n'''',<24>,57:0] MULTI_LINE_COMMENT
[@371,940:940='\n',<3>,62:0] NEWLINE
[@372,942:942='\n',<3>,63:0] NEWLINE
[@373,943:947='while',<19>,63:0] WHILE
[@374,948:948=' ',<30>,63:5] WS
[@375,949:952='data',<29>,63:6] VARIABLE
[@376,953:953=' ',<30>,63:10] WS
[@377,954:954='>',<16>,63:11] COMPARISON_OP
[@378,955:955=' ',<30>,63:12] WS
[@379,956:956='0',<25>,63:13] NUMBER
[@380,957:957=' ',<30>,63:14] WS
[@381,958:959='or',<17>,63:15] LOGICAL_OP
[@382,960:960=' ',<30>,63:17] WS
[@383,961:964='data',<29>,63:18] VARIABLE
[@384,965:965=' ',<30>,63:22] WS
[@385,966:967='!=',<16>,63:23] COMPARISON_OP
[@386,968:968=' ',<30>,63:25] WS
[@387,969:969='0',<25>,63:26] NUMBER
[@388,970:970=':',<13>,63:27] COLON
[@389,973:973='\t',<3>,64:1] NEWLINE
[@390,973:973='<INDENT>',<1>,63:1] INDENT
[@391,974:977='data',<29>,64:1] VARIABLE
[@392,978:978=' ',<30>,64:5] WS
[@393,979:979='=',<5>,64:6] ASSIGNMENT_OP
[@394,980:980=' ',<30>,64:7] WS
[@395,981:984='data',<29>,64:8] VARIABLE
[@396,985:985=' ',<30>,64:12] WS
[@397,986:986='-',<6>,64:13] ARITHMETIC_OP
[@398,987:987=' ',<30>,64:14] WS
[@399,988:988='1',<25>,64:15] NUMBER
[@400,991:991='\t',<3>,65:1] NEWLINE
[@401,992:993='if',<10>,65:1] IF
[@402,994:994=' ',<30>,65:3] WS
[@403,995:998='True',<26>,65:4] BOOLEAN
[@404,999:999=':',<13>,65:8] COLON
[@405,1003:1003='\t',<3>,66:2] NEWLINE
[@406,1003:1003='<INDENT>',<1>,65:2] INDENT
[@407,1004:1004='a',<29>,66:2] VARIABLE
[@408,1005:1005=' ',<30>,66:3] WS
[@409,1006:1006='=',<5>,66:4] ASSIGNMENT_OP
[@410,1007:1007=' ',<30>,66:5] WS
[@411,1008:1054='"This is the weirdest code I have ever written"',<27>,66:6] STRING
[@412,1056:1056='\n',<3>,67:0] NEWLINE
[@413,1056:1056='<DEDENT>',<2>,66:0] DEDENT
[@414,1056:1056='<DEDENT>',<2>,66:0] DEDENT
[@415,1058:1058='\n',<3>,68:0] NEWLINE
[@416,1059:1061='for',<20>,68:0] FOR
[@417,1062:1062=' ',<30>,68:3] WS
[@418,1063:1066='data',<29>,68:4] VARIABLE
[@419,1067:1067=' ',<30>,68:8] WS
[@420,1068:1069='in',<22>,68:9] IN
[@421,1070:1070=' ',<30>,68:11] WS
[@422,1071:1076='array1',<29>,68:12] VARIABLE
[@423,1077:1077=':',<13>,68:18] COLON
[@424,1080:1080='\t',<3>,69:1] NEWLINE
[@425,1080:1080='<INDENT>',<1>,68:1] INDENT
[@426,1081:1082='if',<10>,69:1] IF
[@427,1083:1083=' ',<30>,69:3] WS
[@428,1084:1087='data',<29>,69:4] VARIABLE
[@429,1088:1088=' ',<30>,69:8] WS
[@430,1089:1089='<',<16>,69:9] COMPARISON_OP
[@431,1090:1090=' ',<30>,69:10] WS
[@432,1091:1091='0',<25>,69:11] NUMBER
[@433,1092:1092=':',<13>,69:12] COLON
[@434,1096:1096='\t',<3>,70:2] NEWLINE
[@435,1096:1096='<INDENT>',<1>,69:2] INDENT
[@436,1097:1101='while',<19>,70:2] WHILE
[@437,1102:1102='(',<14>,70:7] LPAREN
[@438,1103:1106='data',<29>,70:8] VARIABLE
[@439,1107:1107=' ',<30>,70:12] WS
[@440,1108:1109='!=',<16>,70:13] COMPARISON_OP
[@441,1110:1110=' ',<30>,70:15] WS
[@442,1111:1111='0',<25>,70:16] NUMBER
[@443,1112:1112=')',<15>,70:17] RPAREN
[@444,1113:1113=':',<13>,70:18] COLON
[@445,1118:1118='\t',<3>,71:3] NEWLINE
[@446,1118:1118='<INDENT>',<1>,70:3] INDENT
[@447,1119:1119='b',<29>,71:3] VARIABLE
[@448,1120:1120=' ',<30>,71:4] WS
[@449,1121:1121='=',<5>,71:5] ASSIGNMENT_OP
[@450,1122:1122=' ',<30>,71:6] WS
[@451,1123:1156='"This code doesn't make any sense"',<27>,71:7] STRING
[@452,1161:1161='\t',<3>,72:3] NEWLINE
[@453,1162:1165='data',<29>,72:3] VARIABLE
[@454,1166:1166=' ',<30>,72:7] WS
[@455,1167:1167='=',<5>,72:8] ASSIGNMENT_OP
[@456,1168:1168=' ',<30>,72:9] WS
[@457,1169:1172='data',<29>,72:10] VARIABLE
[@458,1173:1173=' ',<30>,72:14] WS
[@459,1174:1174='+',<6>,72:15] ARITHMETIC_OP
[@460,1175:1175=' ',<30>,72:16] WS
[@461,1176:1176='1',<25>,72:17] NUMBER
[@462,1179:1179='\t',<3>,73:1] NEWLINE
[@463,1179:1179='<DEDENT>',<2>,72:1] DEDENT
[@464,1179:1179='<DEDENT>',<2>,72:1] DEDENT
[@465,1180:1183='elif',<11>,73:1] ELIF
[@466,1184:1184=' ',<30>,73:5] WS
[@467,1185:1188='data',<29>,73:6] VARIABLE
[@468,1189:1189=' ',<30>,73:10] WS
[@469,1190:1190='>',<16>,73:11] COMPARISON_OP
[@470,1191:1191=' ',<30>,73:12] WS
[@471,1192:1192='0',<25>,73:13] NUMBER
[@472,1193:1193=':',<13>,73:14] COLON
[@473,1197:1197='\t',<3>,74:2] NEWLINE
[@474,1197:1197='<INDENT>',<1>,73:2] INDENT
[@475,1198:1202='while',<19>,74:2] WHILE
[@476,1203:1203='(',<14>,74:7] LPAREN
[@477,1204:1207='data',<29>,74:8] VARIABLE
[@478,1208:1208=' ',<30>,74:12] WS
[@479,1209:1210='!=',<16>,74:13] COMPARISON_OP
[@480,1211:1211=' ',<30>,74:15] WS
[@481,1212:1212='0',<25>,74:16] NUMBER
[@482,1213:1213=')',<15>,74:17] RPAREN
[@483,1214:1214=':',<13>,74:18] COLON
[@484,1219:1219='\t',<3>,75:3] NEWLINE
[@485,1219:1219='<INDENT>',<1>,74:3] INDENT
[@486,1220:1220='c',<29>,75:3] VARIABLE
[@487,1221:1221=' ',<30>,75:4] WS
[@488,1222:1222='=',<5>,75:5] ASSIGNMENT_OP
[@489,1223:1223=' ',<30>,75:6] WS
[@490,1224:1257='"I feel like I have no purpose..."',<27>,75:7] STRING
[@491,1262:1262='\t',<3>,76:3] NEWLINE
[@492,1263:1266='data',<29>,76:3] VARIABLE
[@493,1267:1267=' ',<30>,76:7] WS
[@494,1268:1268='=',<5>,76:8] ASSIGNMENT_OP
[@495,1269:1269=' ',<30>,76:9] WS
[@496,1270:1273='data',<29>,76:10] VARIABLE
[@497,1274:1274=' ',<30>,76:14] WS
[@498,1275:1275='-',<6>,76:15] ARITHMETIC_OP
[@499,1276:1276=' ',<30>,76:16] WS
[@500,1277:1277='1',<25>,76:17] NUMBER
[@501,1279:1279='\n',<3>,77:0] NEWLINE
[@502,1279:1279='<DEDENT>',<2>,76:0] DEDENT
[@503,1279:1279='<DEDENT>',<2>,76:0] DEDENT
[@504,1279:1279='<DEDENT>',<2>,76:0] DEDENT
[@505,1281:1281='\n',<3>,78:0] NEWLINE
[@506,1282:1284='for',<20>,78:0] FOR
[@507,1285:1285=' ',<30>,78:3] WS
[@508,1286:1286='i',<29>,78:4] VARIABLE
[@509,1287:1287=' ',<30>,78:5] WS
[@510,1288:1289='in',<22>,78:6] IN
[@511,1290:1290=' ',<30>,78:8] WS
[@512,1291:1295='range',<21>,78:9] RANGE
[@513,1296:1296='(',<14>,78:14] LPAREN
[@514,1297:1297='0',<25>,78:15] NUMBER
[@515,1298:1298=',',<9>,78:16] COMMA
[@516,1299:1299='5',<25>,78:17] NUMBER
[@517,1300:1300=')',<15>,78:18] RPAREN
[@518,1301:1301=':',<13>,78:19] COLON
[@519,1304:1304='\t',<3>,79:1] NEWLINE
[@520,1304:1304='<INDENT>',<1>,78:1] INDENT
[@521,1305:1308='data',<29>,79:1] VARIABLE
[@522,1309:1309=' ',<30>,79:5] WS
[@523,1310:1310='=',<5>,79:6] ASSIGNMENT_OP
[@524,1311:1311=' ',<30>,79:7] WS
[@525,1312:1315='data',<29>,79:8] VARIABLE
[@526,1316:1316=' ',<30>,79:12] WS
[@527,1317:1317='*',<6>,79:13] ARITHMETIC_OP
[@528,1318:1318=' ',<30>,79:14] WS
[@529,1319:1319='2',<25>,79:15] NUMBER
[@530,1322:1322='\t',<3>,80:1] NEWLINE
[@531,1323:1326='data',<29>,80:1] VARIABLE
[@532,1327:1327=' ',<30>,80:5] WS
[@533,1328:1328='=',<5>,80:6] ASSIGNMENT_OP
[@534,1329:1329=' ',<30>,80:7] WS
[@535,1330:1333='data',<29>,80:8] VARIABLE
[@536,1334:1334=' ',<30>,80:12] WS
[@537,1335:1335='-',<6>,80:13] ARITHMETIC_OP
[@538,1336:1336=' ',<30>,80:14] WS
[@539,1337:1337='1',<25>,80:15] NUMBER
[@540,1339:1339='\n',<3>,81:0] NEWLINE
[@541,1339:1339='<DEDENT>',<2>,80:0] DEDENT
[@542,1341:1341='\n',<3>,82:0] NEWLINE
[@543,1342:1392='''' I need help, this code shouldn't even exist '''',<24>,82:0] MULTI_LINE_COMMENT
[@544,1394:1394='\n',<3>,83:0] NEWLINE
[@545,1395:1399='while',<19>,83:0] WHILE
[@546,1400:1400=' ',<30>,83:5] WS
[@547,1401:1404='True',<26>,83:6] BOOLEAN
[@548,1405:1405=':',<13>,83:10] COLON
[@549,1408:1408='\t',<3>,84:1] NEWLINE
[@550,1408:1408='<INDENT>',<1>,83:1] INDENT
[@551,1409:1412='data',<29>,84:1] VARIABLE
[@552,1413:1413=' ',<30>,84:5] WS
[@553,1414:1414='=',<5>,84:6] ASSIGNMENT_OP
[@554,1415:1415=' ',<30>,84:7] WS
[@555,1416:1417='30',<25>,84:8] NUMBER
[@556,1420:1420='\t',<3>,85:1] NEWLINE
[@557,1421:1424='data',<29>,85:1] VARIABLE
[@558,1425:1425=' ',<30>,85:5] WS
[@559,1426:1426='=',<5>,85:6] ASSIGNMENT_OP
[@560,1427:1427=' ',<30>,85:7] WS
[@561,1428:1431='data',<29>,85:8] VARIABLE
[@562,1432:1432=' ',<30>,85:12] WS
[@563,1433:1433='-',<6>,85:13] ARITHMETIC_OP
[@564,1434:1434=' ',<30>,85:14] WS
[@565,1435:1435='1',<25>,85:15] NUMBER
[@566,1435:1435='1',<3>,85:16] NEWLINE
[@567,1435:1435='<DEDENT>',<2>,85:16] DEDENT
[@568,1435:1435='<DEDENT>',<2>,85:16] DEDENT
[@569,1431:1435='a - 1',<-1>,85:16] WS_SKIPPED
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
            (comment # Deliverable 1)) \n 
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
            (comment # Deliverable 2)) \n \n 
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
                                 (value flag)))) ))   and   
                  (comparison_condition 
                     (value var3))   >   
                  (comparison_condition 
                     (value 10))) : \t 
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
                              (value -1)))) \n) <DEDENT>)))) \n 
      (line 
         (comment # Deliverable 3)) \n \n 
      (line 
         (comment ## comment test 1)) \n \n 
      (line 
         (comment ''' \r\n\tcomment test 2\r\n\tadding more comments\r\n\tand more...\r\n''')) \n \n 
      (line 
         (while_block while   
            (condition 
               (comparison_condition 
                  (value data))   >   
               (comparison_condition 
                  (value 0))   or   
               (comparison_condition 
                  (value data))   !=   
               (comparison_condition 
                  (value 0))) : \t 
            (block <INDENT> 
               (first_block 
                  (line 
                     (assignment data   
                        (assignment_operator =)   
                        (expression 
                           (value data)   
                           (operator -)   
                           (value 1)))) \t 
                  (line 
                     (if_block if   
                        (condition 
                           (comparison_condition 
                              (value True))) : \t 
                        (block <INDENT> 
                           (first_block 
                              (line 
                                 (assignment a   
                                    (assignment_operator =)   
                                    (expression 
                                       (value "This is the weirdest code I have ever written")))) \n) <DEDENT>)))) <DEDENT>))) \n 
      (line 
         (for_block for   
            (for_condition data   in   
               (iterable array1)) : \t 
            (block <INDENT> 
               (first_block 
                  (line 
                     (if_block if   
                        (condition 
                           (comparison_condition 
                              (value data))   <   
                           (comparison_condition 
                              (value 0))) : \t 
                        (block <INDENT> 
                           (first_block 
                              (line 
                                 (while_block while 
                                    (condition 
                                       (comparison_condition ( 
                                          (condition 
                                             (comparison_condition 
                                                (value data))   !=   
                                             (comparison_condition 
                                                (value 0))) ))) : \t 
                                 (block <INDENT> 
                                    (first_block 
                                       (line 
                                          (assignment b   
                                             (assignment_operator =)   
                                             (expression 
                                                (value "This code doesn't make any sense")))) \t 
                                       (line 
                                          (assignment data   
                                             (assignment_operator =)   
                                             (expression 
                                                (value data)   
                                                (operator +)   
                                                (value 1)))) \t) <DEDENT>)))) <DEDENT>) 
                     (elif_block elif 
                        (condition   
                           (comparison_condition 
                              (value data))   >   
                           (comparison_condition 
                              (value 0))) : \t 
                        (block <INDENT> 
                           (first_block 
                              (line 
                                 (while_block while 
                                    (condition 
                                       (comparison_condition ( 
                                          (condition 
                                             (comparison_condition 
                                                (value data))   !=   
                                             (comparison_condition 
                                                (value 0))) ))) : \t 
                                 (block <INDENT> 
                                    (first_block 
                                       (line 
                                          (assignment c   
                                             (assignment_operator =)   
                                             (expression 
                                                (value "I feel like I have no purpose...")))) \t 
                                       (line 
                                          (assignment data   
                                             (assignment_operator =)   
                                             (expression 
                                                (value data)   
                                                (operator -)   
                                                (value 1)))) \n) <DEDENT>)))) <DEDENT>))))) <DEDENT>))) \n 
   (line 
      (for_block for   
         (for_condition i   in   
            (iterable range ( 
               (count 0) , 
               (count 5) ))) : \t 
      (block <INDENT> 
         (first_block 
            (line 
               (assignment data   
                  (assignment_operator =)   
                  (expression 
                     (value data)   
                     (operator *)   
                     (value 2)))) \t 
            (line 
               (assignment data   
                  (assignment_operator =)   
                  (expression 
                     (value data)   
                     (operator -)   
                     (value 1)))) \n) <DEDENT>))) \n 
   (line 
      (comment ''' I need help, this code shouldn't even exist ''')) \n 
   (line 
      (while_block while   
         (condition 
            (comparison_condition 
               (value True))) : \t 
         (block <INDENT> 
            (first_block 
               (line 
                  (assignment data   
                     (assignment_operator =)   
                     (expression 
                        (value 30)))) \t 
               (line 
                  (assignment data   
                     (assignment_operator =)   
                     (expression 
                        (value data)   
                        (operator -)   
                        (value 1)))) 1) <DEDENT>)))) <DEDENT> a - 1))

Project Deliverable 3: Passed
```