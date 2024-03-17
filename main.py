import yaml
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])

css_selector = "span.mdc-text-field__ripple"

print(site.get_element_property("css", css_selector, "height"))

xpath = '//*[@id="login"]/div[2]/button/div'

print(site.get_element_property("xpath", xpath, "color"))

# i feel like the way my final exam-like assignments for my coding and testing specialty were says a lot about... the specialties themselves. like coding which was the first i took right,
# it was basically just things you would know if you did the midterm projects. and you have to do the midterms to get to the final, and there were like 9 questions total.
# granted you needed like what 8 questions right to pass, but it's not THAT much like it's feasible to do in the 20 minute time frame they gave us.

# then there's the testing specialty final. 150 questions, 100 needed to pass, 200 minutes given. most questions were from deep-dives on one particular testing topic that you wouldn't know the answer to
# if you didn't write your thesis on the topic. i passed with 109 questions right, but that was INTENSE?? i mean yea half the intensity was from copy-pasting questions into google but it still WAS??\

# i just hope the analytics speacialty will go easy on me i did not learn anything and i doubt google will have solid answers for the obscure questions they already ask me on that specialty.
