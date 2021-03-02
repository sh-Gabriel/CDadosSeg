from enum import Enum

class M_data(Enum):
    AUTHOR = 0
    LINK = 1
    CATEGORY = 2
    DATE = 3
    #number of tokens
    NUM_TOKENS = 4
    #number of words without punctuation
    NUM_WITHOUT_PONCT = 5
    #number of types
    NUM_TYPES = 6
    #number of links inside the news
    NUM_LINKS = 7
    #number of words in upper case
    NUM_UPPERCASE = 8
    #number of verbs
    NUM_VERBS = 9
    #number of subjuntive and imperative verbs
    NUM_SUBJ_IMP = 10
    #number of nouns
    NUM_NOUNS = 11
    #number of adjectives
    NUM_ADJ = 12
    #number of adverbs
    NUM_ADV = 13
    #number of modal verbs (mainly auxiliary verbs)
    NUM_MODAL = 14
    #number of singular first and second personal pronouns
    NUM_SPSPP = 15
    #number of plural first personal pronouns
    NUM_PFPP = 16
    #number of pronouns
    NUM_PRONOUNS = 17
    PAUSALITY = 18
    NUM_CHAR = 19
    AVG_SENT_LEN = 20
    AVG_WORD_LEN = 21
    SPEL_ERROR = 22
    EMOTIVENESS = 23
    DIVERSITY = 24