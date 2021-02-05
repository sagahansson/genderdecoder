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
