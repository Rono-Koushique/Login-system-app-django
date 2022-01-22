def unique_validate(self, username, email):
        username_exists = User.objects.get(username=username)
        email_exists = User.objects.get(email=email)
        if username_exists or email_exists:
            return False
        else:
            return True

unique_validate(self, "sanyman", "sagerobi@gmail.com")