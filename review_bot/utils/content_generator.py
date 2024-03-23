```python
import random
from review_bot.config.settings import WEBSITE_URLS

class ContentGenerator:
    def __init__(self):
        # Predefined sets of words to generate review content
        self.adjectives = ["great", "amazing", "pleasant", "excellent", "good"]
        self.nouns = ["service", "experience", "product", "quality", "support"]
        self.verbs = ["had", "experienced", "received", "enjoyed", "found"]
        self.conclusions = [
            "Would recommend to everyone!",
            "Will definitely come back again.",
            "I'm very satisfied.",
            "Thumbs up!",
            "Keep up the good work!"
        ]

    def generate_review_content(self):
        # Randomly select words from the predefined sets to construct a review
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        verb = random.choice(self.verbs)
        conclusion = random.choice(self.conclusions)

        # Construct the review content
        review = f"I {verb} a {adjective} {noun}. {conclusion}"

        return review

# Example usage:
# content_generator = ContentGenerator()
# review_content = content_generator.generate_review_content()
# print(review_content)
```