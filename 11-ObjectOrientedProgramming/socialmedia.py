class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f'{self.username} posts:')
        print(*[f"{i + 1}.{post}\n" for i,post in enumerate(self.posts)])

def main():
    user1 = SocialMediaProfile('johndoe')
    user1.add_post("Hello, world!")
    user1.add_post("Had a great day at the park!")
    user1.add_post("What's up, Natalie? How are you?")
    user1.display_timeline()

if __name__ == "__main__":
    main()