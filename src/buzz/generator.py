"""
Create a little buzz generator.
"""
import random


buzz = ('continuous testing', 'continuous integration',
        'continuous deployment', 'continuous improvement', 'devops')
adjectives = ('complete', 'modern', 'self-service',
              'integrated', 'end-to-end')
adverbs = ('remarkably', 'enormously', 'substantially',
           'significantly', 'seriously')

verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')


def sample(list_, n=1):
    """Generate ci/cd phrases"""
    result = random.sample(list_, n)
    if n == 1:
        return result[0]
    return result

def generate_buzz():
    """Generate ci/cd phrases"""
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
                       sample(verbs), buzz_terms[1]])
    return phrase.title()

def pointless_function(num1,num2):
    """Function for demonstrate unittests"""
    result = num1 * num2
    return result

if __name__ == "__main__":
    print(generate_buzz())