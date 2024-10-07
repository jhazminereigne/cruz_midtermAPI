import faker

fake = faker.Faker()


profiles = []
for _ in range(10):
    profile = {
        "full_name": fake.name(),
        "email": fake.email(),
        "job_title": fake.job(),
        "company": fake.company()
    }
    profiles.append(profile)


for profile in profiles:
    print(f"Full Name: {profile['full_name']}, Email: {profile['email']}, Job Title: {profile['job_title']}, Company: {profile['company']}")