
# first install camel-tools on the command line:
# pip install camel-tools

# full installation instructions: https://github.com/CAMeL-Lab/camel_tools

# camel-tools needs additional data for some of its functionality.
# Run this command in the command line:
# camel_data light
# (NB: if this does not work: try `camel_data -i light`)

# This installs only the necessary data for morphology and MLE disambiguation;
# to install all data (for dialect recognition, sentiment analysis, etc.):
# WARNING: more than a gigabyte of data!
# run this command in the command line:
# camel_data -i all

# documentation: https://camel-tools.readthedocs.io/en/stable/
# tutorial: https://colab.research.google.com/drive/1Y3qCbD6Gw1KEw-lixQx1rI6WlyWnrnDS?usp=sharing#scrollTo=Upf_eeVE0889


from camel_tools.disambig.mle import MLEDisambiguator
import regex


text = """هل تحتاج إلى ترجمة كي تفهم خطاب الملك؟ اللغة "الكلاسيكية"\
(الفصحى) موجودة في كل اللغات وكذلك اللغة "الدارجة" \
.. الفرنسية التي ندرس في المدرسة ليست الفرنسية التي يستخدمها \
الناس في شوارع باريس .. وملكة بريطانيا لا تخطب بلغة شوارع لندن .. لكل مقام مقال"""


# the text needs to be tokenized first:
tokens = regex.findall("\w+", text)

# camel-tools uses a disambiguator to determine the most likely analysis/reading
# of a word in a given context, using a Maximum Likelihood Estimation model:

mle = MLEDisambiguator.pretrained()
disambig = mle.disambiguate(tokens)


# For each disambiguated word d in disambig, d.analyses is a list of analyses
# sorted from most likely to least likely. Therefore, d.analyses[0] would
# be the most likely analysis for a given word.
# For each analysis, camel-tools offers us the lexeme ("lex"),
# a vowelled/diacriticized version ("diac"), and its part of speech ("pos").
lemmas = []
for d in disambig:
    # use the lexeme of the most probable reading of the token as its lemma:
    lemma = d.analyses[0].analysis['lex']
    lemmas.append(lemma)
print(lemmas)
# ['هَل', 'ٱِحْتاج', 'إِلَى', 'تَرْجَمَة', 'كَي', 'فَهِم', 'خِطاب', 'مَلِك', '؟',
#  'لُغَة', '"', 'كلاسِيكِيّ', '"', '(', 'فُصْحَى', ')', 'مَوْجُود', 'فِي', 'كُلّ',
#  'لُغَة', 'ذٰلِكَ', 'لُغَة', '"', 'دارِج', '"', '.', '.', 'فَرَنْسِيّ', 'الَّذِي',
#  'دَرَس', 'فِي', 'مَدْرَسَة', 'لَيِس', 'فَرَنْسِيّ', 'الَّذِي', 'ٱِسْتَخْدَم', 'ناس',
#  'فِي', 'شارِع', 'بارِيس', '.', '.', 'مَلَك', 'برِيطانِيا', 'لا', 'خَطَب',
#  'لُغَة', 'شارِع', 'لَنْدَن', '.', '.', 'كُلّ', 'مَقام', 'مَقال']
# => perfect!

# we can also do this in one line of code, using list comprehension:
lemmas = [d.analyses[0].analysis['lex'] for d in disambig]

# Note that the lemma contains vowels and other diacritics;
# we will remove these:

from camel_tools.utils.dediac import dediac_ar

lemmas = []
for d in disambig:
    # use the lexeme of the most probable reading of the token as its lemma:
    lemma = d.analyses[0].analysis['lex']
    # remove the diacritics:
    lemma_without_vowels = dediac_ar(lemma)
    lemmas.append(lemma_without_vowels)
print(lemmas)
# ['هل', 'ٱحتاج', 'إلى', 'ترجمة', 'كي', 'فهم', 'خطاب', 'ملك', 'لغة',
#  'كلاسيكي', 'فصحى', 'موجود', 'في', 'كل', 'لغة', 'ذلك', 'لغة', 'دارج',
#  'فرنسي', 'الذي', 'درس', 'في', 'مدرسة', 'ليس', 'فرنسي', 'الذي', 'ٱستخدم',
#  'ناس', 'في', 'شارع', 'باريس', 'ملك', 'بريطانيا', 'لا', 'خطب', 'لغة',
#  'شارع', 'لندن', 'كل', 'مقام', 'مقال']



