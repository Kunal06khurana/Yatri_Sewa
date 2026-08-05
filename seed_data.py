import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from accounts.models import Accommodation

def create_seed_data():
    # Clear existing accommodations to avoid duplicates
    Accommodation.objects.all().delete()
    print("Cleared existing accommodations.")

    hotels = [
        {
            'name': 'Royal Heritage Camp',
            'location': 'Sector 1, Prayagraj',
            'price': 4500.00,
            'description': 'A luxurious camp experience with premium amenities, offering a royal stay amidst the spiritual atmosphere of Kumbh Mela.',
            'availability': True,
        },
        {
            'name': 'Ganga View Retreat',
            'location': 'Sangam Bank, Prayagraj',
            'price': 3200.00,
            'description': 'Wake up to breathtaking views of the sacred Ganga river. A peaceful retreat with modern comforts and traditional decor.',
            'availability': True,
        },
        {
            'name': 'Triveni Tent Resort',
            'location': 'Sector 5, Prayagraj',
            'price': 2800.00,
            'description': 'Comfortable tent accommodations at the confluence of three sacred rivers. Perfect for pilgrims seeking a spiritual journey.',
            'availability': True,
        },
        {
            'name': 'Prayag Grand Hotel',
            'location': 'Civil Lines, Prayagraj',
            'price': 5500.00,
            'description': 'A full-service hotel with air-conditioned rooms, restaurant, and easy access to the main Kumbh Mela bathing ghats.',
            'availability': True,
        },
        {
            'name': 'Mela Eco Cottage',
            'location': 'Sector 12, Prayagraj',
            'price': 1800.00,
            'description': 'Eco-friendly cottages built with sustainable materials. Experience nature while staying close to all the main Mela activities.',
            'availability': True,
        },
        {
            'name': 'Deluxe Pilgrim Camp',
            'location': 'Sector 8, Prayagraj',
            'price': 2500.00,
            'description': 'Specially designed camps for pilgrims with clean facilities, hot water, and wholesome meals included in the package.',
            'availability': True,
        },
    ]

    for hotel_data in hotels:
        acc = Accommodation.objects.create(**hotel_data)
        print(f"Created: {acc.name} (ID: {acc.id})")

    print(f"\nSuccessfully created {len(hotels)} accommodations!")
    print("You can now visit your site to see all the accommodations.")

if __name__ == '__main__':
    create_seed_data()