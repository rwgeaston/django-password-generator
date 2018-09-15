big_input = '''The Project Gutenberg EBook of The Adventures of Sherlock Holmes
by Sir Arthur Conan Doyle
(#15 in our series by Sir Arthur Conan Doyle)

Copyright laws are changing all over the world. Be sure to check the
copyright laws for your country before downloading or redistributing
this or any other Project Gutenberg eBook.

This header should be the first thing seen when viewing this Project
Gutenberg file.  Please do not remove it.  Do not change or edit the
header without written permission.

Please read the "legal small print," and other information about the
eBook and Project Gutenberg at the bottom of this file.  Included is
important information about your specific rights and restrictions in
how the file may be used.  You can also find out about how to make a
donation to Project Gutenberg, and how to get involved.


**Welcome To The World of Free Plain Vanilla Electronic Texts**

**eBooks Readable By Both Humans and By Computers, Since 1971**

*****These eBooks Were Prepared By Thousands of Volunteers!*****


Title: The Adventures of Sherlock Holmes

Author: Sir Arthur Conan Doyle

Release Date: March, 1999  [EBook #1661]
[Most recently updated: November 29, 2002]

Edition: 12

Language: English

Character set encoding: ASCII

*** START OF THE PROJECT GUTENBERG EBOOK, THE ADVENTURES OF SHERLOCK HOLMES ***




(Additional editing by Jose Menendez)



THE ADVENTURES OF
SHERLOCK HOLMES

BY

SIR ARTHUR CONAN DOYLE

CONTENTS

I.	A Scandal in Bohemia
II.	The Red-Headed League
III.	A Case of Identity
IV.	The Boscombe Valley Mystery
V.	The Five Orange Pips
VI.	The Man with the Twisted Lip
VII.	The Adventure of the Blue Carbuncle
VIII.	The Adventure of the Speckled Band
IX.	The Adventure of the Engineer's Thumb
X.	The Adventure of the Noble Bachelor
XI.	The Adventure of the Beryl Coronet
XII.	The Adventure of the Copper Beeches


ADVENTURE  I.  A SCANDAL IN BOHEMIA

I.


To Sherlock Holmes she is always the woman. I have seldom heard him mention her under any other name. In his eyes she eclipses and predominates the whole of her sex. It was not that he felt any emotion akin to love for Irene Adler. All emotions, and that one particularly, were abhorrent to his cold, precise but admirably balanced mind. He was, I take it, the most perfect reasoning and observing machine that the world has seen, but as a lover he would have placed himself in a false position. He never spoke of the softer passions, save with a gibe and a sneer. They were admirable things for the observer--excellent for drawing the veil from men's motives and actions. But for the trained reasoner to admit such intrusions into his own delicate and finely adjusted temperament was to introduce a distracting factor which might throw a doubt upon all his mental results. Grit in a sensitive instrument, or a crack in one of his own high-power lenses, would not be more disturbing than a strong emotion in a nature such as his. And yet there was but one woman to him, and that woman was the late Irene Adler, of dubious and questionable memory.

I had seen little of Holmes lately. My marriage had drifted us away from each other. My own complete happiness, and the home-centred interests which rise up around the man who first finds himself master of his own establishment, were sufficient to absorb all my attention, while Holmes, who loathed every form of society with his whole Bohemian soul, remained in our lodgings in Baker Street, buried among his old books, and alternating from week to week between cocaine and ambition, the drowsiness of the drug, and the fierce energy of his own keen nature. He was still, as ever, deeply attracted by the study of crime, and occupied his immense faculties and extraordinary powers of observation in following out those clues, and clearing up those mysteries which had been abandoned as hopeless by the official police. From time to time I heard some vague account of his doings: of his summons to Odessa in the case of the Trepoff murder, of his clearing up of the singular tragedy of the Atkinson brothers at Trincomalee, and finally of the mission which he had accomplished so delicately and successfully for the reigning family of Holland. Beyond these signs of his activity, however, which I merely shared with all the readers of the daily press, I knew little of my former friend and companion.

One night--it was on the twentieth of March, 1888--I was returning from a journey to a patient (for I had now returned to civil practice), when my way led me through Baker Street. As I passed the well-remembered door, which must always be associated in my mind with my wooing, and with the dark incidents of the Study in Scarlet, I was seized with a keen desire to see Holmes again, and to know how he was employing his extraordinary powers. His rooms were brilliantly lit, and, even as I looked up, I saw his tall, spare figure pass twice in a dark silhouette against the blind. He was pacing the room swiftly, eagerly, with his head sunk upon his chest and his hands clasped behind him. To me, who knew his every mood and habit, his attitude and manner told their own story. He was at work again. He had risen out of his drug-created dreams and was hot upon the scent of some new problem. I rang the bell and was shown up to the chamber which had formerly been in part my own.

His manner was not effusive. It seldom was; but he was glad, I think, to see me. With hardly a word spoken, but with a kindly eye, he waved me to an armchair, threw across his case of cigars, and indicated a spirit case and a gasogene in the corner. Then he stood before the fire and looked me over in his singular introspective fashion.

"Wedlock suits you," he remarked. "I think, Watson, that you have put on seven and a half pounds since I saw you."'''

big_output = {
    'the': 67, 'project': 6, 'gutenberg': 6, 'ebook': 5, 'of': 43, 'adventures': 4, 'sherlock': 5, 'holmes': 8,
    'by': 9, 'sir': 4, 'arthur': 4, 'conan': 4, 'doyle': 4, '15': 1, 'in': 19, 'our': 2, 'series': 1, 'copyright': 2,
    'laws': 2, 'are': 1, 'changing': 1, 'all': 5, 'over': 2, 'world': 3, 'be': 5, 'sure': 1, 'to': 23, 'check': 1,
    'for': 7, 'your': 2, 'country': 1, 'before': 2, 'downloading': 1, 'or': 4, 'redistributing': 1, 'this': 4, 'any': 3,
    'other': 4, 'header': 2, 'should': 1, 'first': 2, 'thing': 1, 'seen': 3, 'when': 2, 'viewing': 1, 'file': 3,
    'please': 2, 'do': 2, 'not': 5, 'remove': 1, 'it': 4, 'change': 1, 'edit': 1, 'without': 1, 'written': 1,
    'permission': 1, 'read': 1, 'legal': 1, 'small': 1, 'print': 1, 'and': 36, 'information': 2, 'about': 3,
    'at': 3, 'bottom': 1, 'included': 1, 'is': 2, 'important': 1, 'specific': 1, 'rights': 1, 'restrictions': 1,
    'how': 4, 'may': 1, 'used': 1, 'you': 4, 'can': 1, 'also': 1, 'find': 1, 'out': 3, 'make': 1, 'a': 23,
    'donation': 1, 'get': 1, 'involved': 1, 'welcome': 1, 'free': 1, 'plain': 1, 'vanilla': 1, 'electronic': 1,
    'texts': 1, 'ebooks': 2, 'readable': 1, 'both': 1, 'humans': 1, 'computers': 1, 'since': 2, '1971': 1,
    'these': 2, 'were': 5, 'prepared': 1, 'thousands': 1, 'volunteers': 1, 'title': 1, 'author': 1, 'release': 1,
    'date': 1, 'march': 2, '1999': 1, '1661': 1, 'most': 2, 'recently': 1, 'updated': 1, 'november': 1, '29': 1,
    '2002': 1, 'edition': 1, '12': 1, 'language': 1, 'english': 1, 'character': 1, 'set': 1, 'encoding': 1, 'ascii': 1,
    'start': 1, 'additional': 1, 'editing': 1, 'jose': 1, 'menendez': 1, 'contents': 1, 'i': 18, 'scandal': 2,
    'bohemia': 2, 'ii': 1, 'red-headed': 1, 'league': 1, 'iii': 1, 'case': 4, 'identity': 1, 'iv': 1, 'boscombe': 1,
    'valley': 1, 'mystery': 1, 'v': 1, 'five': 1, 'orange': 1, 'pips': 1, 'vi': 1, 'man': 2, 'with': 10, 'twisted': 1,
    'lip': 1, 'vii': 1, 'adventure': 7, 'blue': 1, 'carbuncle': 1, 'viii': 1, 'speckled': 1, 'band': 1, 'ix': 1,
    'engineers': 1, 'thumb': 1, 'x': 1, 'noble': 1, 'bachelor': 1, 'xi': 1, 'beryl': 1, 'coronet': 1, 'xii': 1,
    'copper': 1, 'beeches': 1, 'she': 2, 'always': 2, 'woman': 3, 'have': 3, 'seldom': 2, 'heard': 2, 'him': 3,
    'mention': 1, 'her': 2, 'under': 1, 'name': 1, 'his': 27, 'eyes': 1, 'eclipses': 1, 'predominates': 1, 'whole': 2,
    'sex': 1, 'was': 17, 'that': 5, 'he': 14, 'felt': 1, 'emotion': 2, 'akin': 1, 'love': 1, 'irene': 2, 'adler': 2,
    'emotions': 1, 'one': 4, 'particularly': 1, 'abhorrent': 1, 'cold': 1, 'precise': 1, 'but': 6, 'admirably': 1,
    'balanced': 1, 'mind': 2, 'take': 1, 'perfect': 1, 'reasoning': 1, 'observing': 1, 'machine': 1, 'has': 1, 'as': 6,
    'lover': 1, 'would': 2, 'placed': 1, 'himself': 2, 'false': 1, 'position': 1, 'never': 1, 'spoke': 1, 'softer': 1,
    'passions': 1, 'save': 1, 'gibe': 1, 'sneer': 1, 'they': 1, 'admirable': 1, 'things': 1, 'drawing': 1, 'veil': 1,
    'from': 5, 'mens': 1, 'motives': 1, 'actions': 1, 'trained': 1, 'reasoner': 1, 'admit': 1, 'such': 2,
    'intrusions': 1, 'into': 1, 'own': 7, 'delicate': 1, 'finely': 1, 'adjusted': 1, 'temperament': 1, 'introduce': 1,
    'distracting': 1, 'factor': 1, 'which': 7, 'might': 1, 'throw': 1, 'doubt': 1, 'upon': 3, 'mental': 1, 'results': 1,
    'grit': 1, 'sensitive': 1, 'instrument': 1, 'crack': 1, 'high-power': 1, 'lenses': 1, 'more': 1, 'disturbing': 1,
    'than': 1, 'strong': 1, 'nature': 2, 'yet': 1, 'there': 1, 'late': 1, 'dubious': 1, 'questionable': 1, 'memory': 1,
    'had': 7, 'little': 2, 'lately': 1, 'my': 8, 'marriage': 1, 'drifted': 1, 'us': 1, 'away': 1, 'each': 1,
    'complete': 1, 'happiness': 1, 'home-centred': 1, 'interests': 1, 'rise': 1, 'up': 5, 'around': 1, 'who': 3,
    'finds': 1, 'master': 1, 'establishment': 1, 'sufficient': 1, 'absorb': 1, 'attention': 1, 'while': 1, 'loathed': 1,
    'every': 2, 'form': 1, 'society': 1, 'bohemian': 1, 'soul': 1, 'remained': 1, 'lodgings': 1, 'baker': 2,
    'street': 2, 'buried': 1, 'among': 1, 'old': 1, 'books': 1, 'alternating': 1, 'week': 2, 'between': 1, 'cocaine': 1,
    'ambition': 1, 'drowsiness': 1, 'drug': 1, 'fierce': 1, 'energy': 1, 'keen': 2, 'still': 1, 'ever': 1, 'deeply': 1,
    'attracted': 1, 'study': 2, 'crime': 1, 'occupied': 1, 'immense': 1, 'faculties': 1, 'extraordinary': 2,
    'powers': 2, 'observation': 1, 'following': 1, 'those': 2, 'clues': 1, 'clearing': 2, 'mysteries': 1, 'been': 2,
    'abandoned': 1, 'hopeless': 1, 'official': 1, 'police': 1, 'time': 2, 'some': 2, 'vague': 1, 'account': 1,
    'doings': 1, 'summons': 1, 'odessa': 1, 'trepoff': 1, 'murder': 1, 'singular': 2, 'tragedy': 1, 'atkinson': 1,
    'brothers': 1, 'trincomalee': 1, 'finally': 1, 'mission': 1, 'accomplished': 1, 'so': 1, 'delicately': 1,
    'successfully': 1, 'reigning': 1, 'family': 1, 'holland': 1, 'beyond': 1, 'signs': 1, 'activity': 1, 'however': 1,
    'merely': 1, 'shared': 1, 'readers': 1, 'daily': 1, 'press': 1, 'knew': 2, 'former': 1, 'friend': 1, 'companion': 1,
    'night--it': 1, 'on': 2, 'twentieth': 1, '1888--i': 1, 'returning': 1, 'journey': 1, 'patient': 1, 'now': 1,
    'returned': 1, 'civil': 1, 'practice': 1, 'way': 1, 'led': 1, 'me': 5, 'through': 1, 'passed': 1,
    'well-remembered': 1, 'door': 1, 'must': 1, 'associated': 1, 'wooing': 1, 'dark': 2, 'incidents': 1, 'scarlet': 1,
    'seized': 1, 'desire': 1, 'see': 2, 'again': 2, 'know': 1, 'employing': 1, 'rooms': 1, 'brilliantly': 1, 'lit': 1,
    'even': 1, 'looked': 2, 'saw': 2, 'tall': 1, 'spare': 1, 'figure': 1, 'pass': 1, 'twice': 1, 'silhouette': 1,
    'against': 1, 'blind': 1, 'pacing': 1, 'room': 1, 'swiftly': 1, 'eagerly': 1, 'head': 1, 'sunk': 1, 'chest': 1,
    'hands': 1, 'clasped': 1, 'behind': 1, 'mood': 1, 'habit': 1, 'attitude': 1, 'manner': 2, 'told': 1, 'their': 1,
    'story': 1, 'work': 1, 'risen': 1, 'drug-created': 1, 'dreams': 1, 'hot': 1, 'scent': 1, 'new': 1, 'problem': 1,
    'rang': 1, 'bell': 1, 'shown': 1, 'chamber': 1, 'formerly': 1, 'part': 1, 'effusive': 1, 'glad': 1, 'think': 2,
    'hardly': 1, 'word': 1, 'spoken': 1, 'kindly': 1, 'eye': 1, 'waved': 1, 'an': 1, 'armchair': 1, 'threw': 1,
    'across': 1, 'cigars': 1, 'indicated': 1, 'spirit': 1, 'gasogene': 1, 'corner': 1, 'then': 1, 'stood': 1, 'fire': 1,
    'introspective': 1, 'fashion': 1, 'wedlock': 1, 'suits': 1, 'remarked': 1, 'watson': 1, 'put': 1, 'seven': 1,
    'half': 1, 'pounds': 1
}
