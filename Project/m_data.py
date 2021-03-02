from enum import Enum

class M_data(Enum):
    AUTHOR = 0
    LINK = 1
    CATEGORY = 2
    DATE = 3
    NUM_TOKENS = 4
    NUM_WITHOUT_PONCT = 5
    NUM_TYPES = 6
    NUM_LINKS = 7
    NUM_UPPERCASE = 8
    NUM_VERBS = 9
    NUM_SUBJ_IMP = 10
    NUM_NOUNS = 11
    NUM_ADJ = 12
    NUM_ADV = 13
    NUM_MODAL = 14
    #number of singular first and second personal pronouns
    NUM_SPSPP = 15
    #number of plural first personal pronouns
    NUM_PFPP = 16
    NUM_PRONOUNS = 17
    PAUSALITY = 18
    NUM_CHAR = 19
    AVG_SENT_LEN = 20
    AVG_WORD_LEN = 21
    SPEL_ERROR = 22
    EMOTIVENESS = 23
    DIVERSITY = 24