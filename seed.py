from database import SessionLocal
from models import Question, Weapon

db = SessionLocal()

db.query(Weapon).delete()
db.query(Question).delete()
db.commit()

weapons_data = [
    {"name": "Combat Knife", "damage": 30, "weapon_type": "Melee", "price": 30},
    {"name": "Pistol", "damage": 45, "weapon_type": "Ranged", "price": 50},
    {"name": "Laser Pistol", "damage": 50, "weapon_type": "Ranged", "price": 150},
    {"name": "Baseball Bat", "damage": 20, "weapon_type": "Melee", "price": 20},
    {"name": "Rifle", "damage": 50, "weapon_type": "Ranged", "price": 100},
    {"name": "Shotgun", "damage": 60, "weapon_type": "Ranged", "price": 80},
]

questions_data = [
    {
        "text": "What was your childhood hobby?",
        "options": [
            {
                "text": "Street fighting",
                "modifiers": {"strength": 1}
            },
            {
                "text": "Hacking school systems",
                "modifiers": {"intelligence": 1}
            },
            {
                "text": "Running in the park",
                "modifiers": {"dexterity": 1}
            }
        ]
    },
    {
        "text": "Your parents were...",
        "options": [
            {
                "text": "Scientists",
                "modifiers": {"intelligence": 1}
            },
            {
                "text": "Traders",
                "modifiers": {"credits": 10}
            },
            {
                "text": "Artists",
                "modifiers": {"charisma": 1}
            }
        ]
    },

    {
        "text": "Your favorite source of information was...",
        "options": [
            {
                "text": "Underground forums",
                "modifiers": {"intelligence": 1}
            },
            {
                "text": "Corporate news feeds",
                "modifiers": {"dexterity": 1}
            },
            {
                "text": "Street gossip",
                "modifiers": {"charisma": 1}
            }
        ]
    },

    {
        "text": "What kind of enhancements did you prefer?",
        "options": [
            {
                "text": "Health boosters",
                "modifiers": {"dexterity": 1}
            },
            {
                "text": "Neural implants",
                "modifiers": {"intelligence": 1}
            },
            {
                "text": "Facial recognition disguises",
                "modifiers": {"charisma": 1}
            }
        ]
    },
    {
        "text": "Your go-to weapon in a confrontation was...",
        "options": [
            {
                "text": "A combat knife",
                "modifiers": {"strength": 1}
            },
            {
                "text": "A hacking device",
                "modifiers": {"intelligence": 1}
            },
            {
                "text": "Smoke grenades",
                "modifiers": {"dexterity": 1}
            }
        ]
    },

    {
        "text": "In your opinion, what the best concept of power in society?",
        "options": [
                {
                    "text": "Something to be challenged through prowess.",
                    "modifiers": {"strength": 1}
                },
            {
                    "text": "Knowledge is the ultimate power.",
                    "modifiers": {"intelligence": 1}
                },
            {
                    "text": "Wealth can accumulate influence.",
                    "modifiers": {"credits": 10}
                }
        ]
    },
    {
        "text": "When navigating the complexities of urban life, what strategy did you find most effective?",
        "options": [
                {
                    "text": "Confronting obstacles with force.",
                    "modifiers": {"strength": 1}
                },
            {
                    "text": "Using cunning and agility.",
                    "modifiers": {"dexterity": 1}
                },
            {
                    "text": "Trying to outsmart rivals.",
                    "modifiers": {"intelligence": 1}
                }
        ]
    },
    {
        "text": "What role did your upbringing play in shaping your approach to conflict resolution?",
        "options": [
                {
                    "text": "I learned to fight.",
                    "modifiers": {"strength": 1}
                },
            {
                    "text": "I preferred to outthink my opponents.",
                    "modifiers": {"intelligence": 1}
                },
            {
                    "text": "Wealth can smooth over many issues.",
                    "modifiers": {"credits": 10}
                }
        ]
    },
    {
        "text": "Reflecting on your past experiences, what do you consider the most valuable lesson learned?",
        "options": [
                {
                    "text": "Strength can be a sword for enemies.",
                    "modifiers": {"strength": 1}
                },
            {
                    "text": "Knowledge is a currency that open doors.",
                    "modifiers": {"intelligence": 1}
                },
            {
                    "text": "Wealth is a powerful tool.",
                    "modifiers": {"credits": 10}
                }
        ]
    },
    {
        "text": "If you could change one aspect of your past, what would it be and why?",
        "options": [
                {
                    "text": "I would have trained harder.",
                    "modifiers": {"dexterity": 1}
                },
            {
                    "text": "I would have sought out more knowledge.",
                    "modifiers": {"intelligence": 1}
                },
            {
                    "text": "I would have focused on building my wealth.",
                    "modifiers": {"credits": 10}
                }
        ]
    }
]


for weapon in weapons_data:
    new_weapon = Weapon(**weapon)
    db.add(new_weapon)

for q in questions_data:
    question = Question(text=q["text"], options=q["options"])
    db.add(question)


try:
    db.commit()
    print("Data seeded successfully!")
except Exception as e:
    db.rollback()
    print(f"Error seeding data: {e}")
finally:
    db.close()
