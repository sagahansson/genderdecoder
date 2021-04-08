import re
import wordlists


def assess(ad_text, masc_w=wordlists.masculine_coded_words, fem_w=wordlists.feminine_coded_words):
    ad_text = ''.join([i if ord(i) < 128 else ' ' for i in ad_text])
    ad_text = re.sub("[\\s]", " ", ad_text, 0, 0)
    ad_text = re.sub("[\.\t\,\:;\(\)\.]", "", ad_text, 0, 0).split(" ")
    ad_text = [ad for ad in ad_text if ad != ""]
        
    masc_w = [adword for adword in ad_text
        for word in masc_w
        if adword.startswith(word)]
    
    fem_w = [adword for adword in ad_text
        for word in fem_w
        if adword.startswith(word)]
    
    if fem_w and not masc_w:
        result = "strongly feminine-coded"
    elif masc_w and not fem_w:
        result = "strongly masculine-coded"
    elif not masc_w and not fem_w:
        result = "neutral"
    else: 
        if len(fem_w) == len(masc_w):
            result = "neutral"
        if ((len(fem_w) / len(masc_w)) >= 2 and 
            len(fem_w) > 5):
            result = "strongly feminine-coded"
        if ((len(masc_w) / len(fem_w)) >= 2 and 
            len(masc_w) > 5):
            result = "strongly masculine-coded"
        if len(fem_w) > len(masc_w):
            result = "feminine-coded"
        if len(masc_w) > len(fem_w):
            result = "masculine-coded"
    
    if "feminine" in result:
        explanation = ("This job ad uses more words that are stereotypically feminine "
            "than words that are stereotypically masculine. Fortunately, the research "
            "suggests this will have only a slight effect on how appealing the job is "
            "to men, and will encourage women applicants.")
    elif "masculine" in result:
        explanation = ("This job ad uses more words that are stereotypically masculine "
            "than words that are stereotypically feminine. It risks putting women off "
            "applying, but will probably encourage men to apply.")
    elif not masc_w and not fem_w:
        explanation = ("This job ad doesn't use any words that are stereotypically "
            "masculine and stereotypically feminine. It probably won't be off-putting "
            "to men or women applicants.")
    else:
        explanation = ("This job ad uses an equal number of words that are "
            "stereotypically masculine and stereotypically feminine. It probably won't "
            "be off-putting to men or women applicants.")

    return {"result": result,
            "explanation": explanation,
            "masculine_coded_words": masc_w,
            "feminine_coded_words": fem_w
            }

# adding the assessing method that Brooke Loveday, the original creator of the genderdecoder algorithm, uses.
def assess_v2(ad_text, masc_w=wordlists.masculine_coded_words, fem_w=wordlists.feminine_coded_words):
    ad_text = ''.join([i if ord(i) < 128 else ' ' for i in ad_text])
    ad_text = re.sub("[\\s]", " ", ad_text, 0, 0)
    ad_text = re.sub("[\.\t\,\:;\(\)\.]", "", ad_text, 0, 0).split(" ")
    ad_text = [ad for ad in ad_text if ad != ""]
        
    masc_w = [adword for adword in ad_text
        for word in masc_w
        if adword.startswith(word)]
    
    fem_w = [adword for adword in ad_text
        for word in fem_w
        if adword.startswith(word)]
    
    fem_w_count = len(fem_w)
    masc_w_count = len(masc_w)
    
    if fem_w_count > masc_w_count:
        result = "feminine-coded"
    elif fem_w_count - masc_w_count == 0:
        result = "neutral"
    else:
        result = "masculine-coded"

    return {"result": result,
            "masculine_coded_words": masc_w,
            "feminine_coded_words": fem_w
            }

# adding the assessing method that Brooke Loveday, the original creator of the genderdecoder algorithm, uses.
#def assess_v2(ad_text, masc_w=wordlists.masculine_coded_words, fem_w=wordlists.feminine_coded_words):
#    ad_text = ''.join([i if ord(i) < 128 else ' ' for i in ad_text])
#    ad_text = re.sub("[\\s]", " ", ad_text, 0, 0)
#    ad_text = re.sub("[\.\t\,\:;\(\)\.]", "", ad_text, 0, 0).split(" ")
#    ad_text = [ad for ad in ad_text if ad != ""]
#        
#    masc_w = [adword for adword in ad_text
#        for word in masc_w
#        if adword.startswith(word)]
#    
#    fem_w = [adword for adword in ad_text
#        for word in fem_w
#        if adword.startswith(word)]
#    
#    fem_w_count = len(fem_w)
#    masc_w_count = len(masc_w)
#    coding_score = fem_w_count - masc_w_count
#    if coding_score == 0:
#        if fem_w_count:
#            result = "neutral"
#        else:
#            result = "empty"
#            
#    elif coding_score > 3:
#        result = "strongly feminine-coded"
#    elif coding_score > 0:
#        result = "feminine-coded"
#    elif coding_score < -3:
#        result = "strongly masculine-coded"
#    else:
#        result = "masculine-coded"
#  

#    return {"result": result,
#            "masculine_coded_words": masc_w,
#            "feminine_coded_words": fem_w
#            }

# male_list and female_list that contain asterisk words should be passed as arguments.
def assess_v3(ad_text, masc_w=wordlists.masculine_coded_words, fem_w=wordlists.feminine_coded_words):
    
    ad_text = ''.join([i if ord(i) < 128 else ' ' for i in ad_text])
    ad_text = re.sub("[\\s]", " ", ad_text, 0, 0)
    ad_text = re.sub("[\.\t\,\:;\(\)\.]", "", ad_text, 0, 0).split(" ")
    ad_text = [ad for ad in ad_text if ad != ""]
    
    masc_asterisk = [w[:-1].lower() for w in masc_w if '*' in w]
    masc_non_asterisk = [w.lower() for w in masc_w if '*' in w]
    
    fem_asterisk = [w[:-1].lower() for w in fem_w if '*' in w]
    fem_non_asterisk = [w.lower() for w in masc_w if '*' in w]
    
    # asterisk words are mapped with all words in the advertisement that start with them.
    masc_w_asterisk = [adword for adword in ad_text
        for word in masc_asterisk
        if adword.startswith(word)]
    
        
    # non asterisk words are mapped with exact occurrences in the advertisement.
    masc_w_non_asterisk = [adword for adword in ad_text
        for word in masc_non_asterisk if adword == word]
    
    # asterisk words are mapped with all words in the advertisement that start with them.    
    fem_w_asterisk = [adword for adword in ad_text
        for word in fem_asterisk
        if adword.startswith(word)]
            
    # non asterisk words are mapped with exact occurrences in the advertisement.
    fem_w_non_asterisk = [adword for adword in ad_text
        for word in fem_non_asterisk
        if adword == word]
    
    all_masc_w = masc_w_asterisk + masc_w_non_asterisk
    all_fem_w = fem_w_asterisk + fem_w_non_asterisk
    
    fem_w_count = len(all_fem_w)
    masc_w_count = len(all_masc_w)
    coding_score = fem_w_count - masc_w_count
    if coding_score == 0:
        if fem_w_count:
            result = "neutral"
        else:
            result = "empty"
            
    elif coding_score > 3:
        result = "strongly feminine-coded"
    elif coding_score > 0:
        result = "feminine-coded"
    elif coding_score < -3:
        result = "strongly masculine-coded"
    else:
        result = "masculine-coded"
        
    return {"result": result,            
            "masculine_coded_words": all_masc_w,
            "feminine_coded_words": all_fem_w
            }


