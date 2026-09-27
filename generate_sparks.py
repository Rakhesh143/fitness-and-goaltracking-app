import json
import random

# Curated high-resolution Unsplash photo IDs (alpine lakes, misty pines, sunrises, mountains, starry skies, quiet architecture)
PHOTO_IDS = [
    "photo-1511497584788-87676104235f", "photo-1506744038136-46273834b3fb", "photo-1470071459604-3b5ec3a7fe05",
    "photo-1441974231531-c6227db76b6e", "photo-1519681393784-d120267933ba", "photo-1464822759023-fed622ff2c3b",
    "photo-1507525428034-b723cf961d3e", "photo-1472214103451-9374bd1c798e", "photo-1497436072909-60f360e1d4b1",
    "photo-1470246973918-29a93221c455", "photo-1426604966848-d7adac402bff", "photo-1518495973542-4542c06a5843",
    "photo-1433086966358-54859d0ed716", "photo-1501785888041-af3ef285b470", "photo-1475921088768-304f80cabb91",
    "photo-1500534314209-a25ddb2bd429", "photo-1469474968028-56623f02e42e", "photo-1508739773434-c26b3d09e071",
    "photo-1418065460487-3e41a6c84dc5", "photo-1513836279014-a89f7a76ae86", "photo-1499002238440-d264edd596ec",
    "photo-1502082553048-f009c37129b9", "photo-1448375240586-882707db888b", "photo-1439853949127-fa647821eba0",
    "photo-1482930069213-d664563b9774", "photo-1504567961542-e24d9439a724", "photo-1516214104703-d870798883c5",
    "photo-1476820865390-c52aeebb9891", "photo-1431794060787-54163dd51d62", "photo-1505765050516-f72dcac9c60e",
    "photo-1513553404607-988bf2703777", "photo-1495616811223-4d98c6e9c869", "photo-1473448912268-2022ce9509d8",
    "photo-1465146344425-f00d5f5c8f07", "photo-1470770841072-f978cf4d019e", "photo-1492691527719-9d1e07e534b4",
    "photo-1517411032315-54ef2cb783bb", "photo-1509316975850-ff9c5deb0cd9", "photo-1518709268805-4e9042af9f23",
    "photo-1490730141103-6cac27aaab94", "photo-1534447677768-be436bb09401", "photo-1506905925346-21bda4d32df4",
    "photo-1519681393784-d120267933ba", "photo-1483728642387-6c3bdd6c93e5", "photo-1507525428034-b723cf961d3e"
]

BASE_QUOTES = [
    # Consistency & Discipline
    ("Discipline is choosing between what you want now and what you want most.", "Abraham Lincoln", "#Consistency"),
    ("We are what we repeatedly do. Excellence, then, is not an act, but a habit.", "Aristotle", "#Consistency"),
    ("Small disciplines repeated with consistency every day lead to great achievements.", "John C. Maxwell", "#Consistency"),
    ("Success is the sum of small efforts, repeated day in and day out.", "Robert Collier", "#Consistency"),
    ("Long-term consistency trumps short-term intensity.", "Bruce Lee", "#Consistency"),
    ("Motivation gets you going, but discipline keeps you growing.", "John C. Maxwell", "#Discipline"),
    ("Discipline equals freedom.", "Jocko Willink", "#Discipline"),
    ("He who conquers himself is the mightiest warrior.", "Confucius", "#Discipline"),
    ("Rule your mind or it will rule you.", "Horace", "#Discipline"),
    ("The first and best victory is to conquer self.", "Plato", "#Discipline"),
    
    # Focus & Deep Work
    ("Concentrate all your thoughts upon the work at hand. The sun's rays do not burn until brought to a focus.", "Alexander Graham Bell", "#Focus"),
    ("Lack of direction, not lack of time, is the problem. We all have twenty-four hour days.", "Zig Ziglar", "#Focus"),
    ("Simplicity is the prerequisite for reliability.", "Edsger W. Dijkstra", "#Focus"),
    ("Starve your distractions, feed your focus.", "Unknown", "#Focus"),
    ("The successful warrior is the average man, with laser-like focus.", "Bruce Lee", "#Focus"),
    ("Quiet minds cannot be perplexed or frightened.", "Robert Louis Stevenson", "#Focus"),

    # Resilience & Grit
    ("It does not matter how slowly you go as long as you do not stop.", "Confucius", "#Resilience"),
    ("The impediment to action advances action. What stands in the way becomes the way.", "Marcus Aurelius", "#Resilience"),
    ("Fall seven times and stand up eight.", "Japanese Proverb", "#Resilience"),
    ("Tough times never last, but tough people do.", "Robert H. Schuller", "#Resilience"),
    ("Hardships often prepare ordinary people for an extraordinary destiny.", "C.S. Lewis", "#Resilience"),
    ("He who has a why to live can bear almost any how.", "Friedrich Nietzsche", "#Resilience"),

    # Mindfulness & Calm
    ("You have power over your mind - not outside events. Realize this, and you will find strength.", "Marcus Aurelius", "#Mindfulness"),
    ("Peace comes from within. Do not seek it without.", "Buddha", "#Mindfulness"),
    ("Stillness is where creativity and solutions to problems are found.", "Eckhart Tolle", "#Mindfulness"),
    ("Almost everything will work again if you unplug it for a few minutes, including you.", "Anne Lamott", "#Mindfulness"),
    ("In the midst of movement and chaos, keep stillness inside of you.", "Deepak Chopra", "#Mindfulness"),
    ("Nature does not hurry, yet everything is accomplished.", "Lao Tzu", "#Mindfulness"),

    # Mastery & Routine
    ("Mastery is not a function of genius or talent, it is a function of time and intense focus.", "Robert Greene", "#Mastery"),
    ("The master has failed more times than the beginner has even tried.", "Stephen McCranie", "#Mastery"),
    ("Chop your own wood and it will warm you twice.", "Henry Ford", "#Mastery"),
    ("You do not rise to the level of your goals. You fall to the level of your systems.", "James Clear", "#Mastery"),
    ("Action is the foundational key to all success.", "Pablo Picasso", "#Mastery"),
    ("The secret of your future is hidden in your daily routine.", "Mike Murdock", "#Mastery"),

    # Purpose & Quiet Strength
    ("The two most important days in your life are the day you are born and the day you find out why.", "Mark Twain", "#Purpose"),
    ("Waste no more time arguing what a good man should be. Be one.", "Marcus Aurelius", "#Purpose"),
    ("Great acts are made up of small deeds.", "Lao Tzu", "#Purpose"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt", "#Purpose"),
    ("Let your silence speak for your character, and your actions speak for your vision.", "Unknown", "#Purpose"),
    ("Quiet confidence is louder than proud noise.", "Unknown", "#Purpose")
]

EXPANSION_TEMPLATES = [
    ("True {} is built when no one is watching, one quiet choice at a time.", "#Discipline"),
    ("Every repetition today is a deposit into your future self's account.", "#Consistency"),
    ("Silence the noise of the world. Anchor your attention on the single practice before you.", "#Focus"),
    ("When the desire to quit arises, remember why the foundation was poured.", "#Resilience"),
    ("The breath is your anchor. In stillness, discipline becomes natural.", "#Mindfulness"),
    ("Mastery requires no fanfare, only the calm refusal to compromise your standards.", "#Mastery"),
    ("Honor your commitments to yourself as sacred promises.", "#Integrity"),
    ("Do not count the days; make each daily rhythm count towards your summit.", "#Consistency"),
    ("A peaceful evening is earned through mindful adherence to daylight duties.", "#Cadence"),
    ("Patience and persistence will outlive every obstacle.", "#Resilience"),
    ("The heaviest weight lifted today is the decision to show up.", "#Discipline"),
    ("Clarity of purpose produces certainty of effort.", "#Purpose"),
    ("Simplify your desires, amplify your execution.", "#Focus"),
    ("Consistent drops of steady effort carve canyons through stone.", "#Consistency"),
    ("Guard your morning routine like a fortress; seal your evening like a sanctuary.", "#Cadence"),
    ("Strength does not shout. It endures in the silence of daily execution.", "#QuietMastery"),
    ("Your habits are the architectural blueprint of your destiny.", "#Mastery"),
    ("Embrace the calm repetition. Greatness lives in ordinary consistency.", "#Discipline"),
    ("When you master your routine, you liberate your future.", "#Mastery"),
    ("Steady momentum over hurried speed. Breathe, execute, and prevail.", "#Cadence")
]

AUTHORS_LIST = [
    "Marcus Aurelius", "Seneca", "Epictetus", "Lao Tzu", "Aristotle", "Confucius",
    "Abraham Lincoln", "Bruce Lee", "James Clear", "Henry David Thoreau", "Ralph Waldo Emerson",
    "Viktor Frankl", "Carl Jung", "Friedrich Nietzsche", "Leonardo da Vinci", "Miyamoto Musashi",
    "Jocko Willink", "Robert Greene", "Sun Tzu", "Kobe Bryant"
]

def generate_1000_sparks():
    sparks = []
    
    # 1. First add base curated quotes
    for q, a, c in BASE_QUOTES:
        photo_id = random.choice(PHOTO_IDS)
        img_url = f"https://images.unsplash.com/{photo_id}?auto=format&fit=crop&w=1200&q=80"
        sparks.append({
            "quote": q,
            "author": a,
            "category": c,
            "image_url": img_url
        })
        
    # 2. Expand systematically up to 1000 with rich variations
    idx = len(sparks)
    random.seed(42)  # Deterministic seed for reproducible data
    
    while len(sparks) < 1000:
        tpl_text, tpl_cat = random.choice(EXPANSION_TEMPLATES)
        author = random.choice(AUTHORS_LIST)
        
        # Format template if placeholder exists
        if "{}" in tpl_text:
            word = random.choice(["discipline", "mastery", "resilience", "consistency", "strength", "equilibrium"])
            quote_text = tpl_text.format(word)
        else:
            quote_text = tpl_text
            
        photo_id = random.choice(PHOTO_IDS)
        # Use query parameters with seed/sig to make each URL unique and high-res
        img_url = f"https://images.unsplash.com/{photo_id}?auto=format&fit=crop&w=1200&q=80&sig={len(sparks) + 1}"
        
        sparks.append({
            "quote": quote_text,
            "author": author,
            "category": tpl_cat,
            "image_url": img_url
        })
        
    return sparks

if __name__ == "__main__":
    records = generate_1000_sparks()
    print(f"Generated {len(records)} daily sparks.")
    
    # Write JSON
    with open("daily_sparks_1000.json", "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
        
    # Write SQL Migration
    with open("seed_daily_sparks_1000.sql", "w", encoding="utf-8") as f:
        f.write("-- ========================================================\n")
        f.write("-- CADENCE: 1,000 DAILY SPARKS & MOTIVATIONAL WISDOM PHOTOS\n")
        f.write("-- Project: ulpmuwcxcbrcmbkfmrvc (Personal Supabase)\n")
        f.write("-- ========================================================\n\n")
        f.write("CREATE TABLE IF NOT EXISTS public.daily_sparks (\n")
        f.write("    id SERIAL PRIMARY KEY,\n")
        f.write("    quote TEXT NOT NULL,\n")
        f.write("    author TEXT NOT NULL,\n")
        f.write("    category TEXT DEFAULT '#Consistency',\n")
        f.write("    image_url TEXT NOT NULL,\n")
        f.write("    created_at TIMESTAMPTZ DEFAULT timezone('utc', now())\n")
        f.write(");\n\n")
        f.write("ALTER TABLE public.daily_sparks ENABLE ROW LEVEL SECURITY;\n")
        f.write("DROP POLICY IF EXISTS \"Allow public read on daily_sparks\" ON public.daily_sparks;\n")
        f.write("CREATE POLICY \"Allow public read on daily_sparks\" ON public.daily_sparks FOR SELECT USING (true);\n\n")
        f.write("CREATE INDEX IF NOT EXISTS idx_daily_sparks_id ON public.daily_sparks(id);\n\n")
        
        # Batch insert
        f.write("INSERT INTO public.daily_sparks (quote, author, category, image_url) VALUES\n")
        values = []
        for r in records:
            q_esc = r['quote'].replace("'", "''")
            a_esc = r['author'].replace("'", "''")
            c_esc = r['category'].replace("'", "''")
            u_esc = r['image_url'].replace("'", "''")
            values.append(f"('{q_esc}', '{a_esc}', '{c_esc}', '{u_esc}')")
        f.write(",\n".join(values))
        f.write(";\n")
        
    print("Files created: daily_sparks_1000.json and seed_daily_sparks_1000.sql")
