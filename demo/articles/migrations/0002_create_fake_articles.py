# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import timedelta
import random

from django.db import models, migrations
from django.utils import timezone


WORDLIST = (
    "ability", "able", "aboard", "about", "above", "accept", "accident", "according", "account", "accurate",
    "adventure", "advice", "affect", "afraid", "after", "afternoon", "again", "against", "age", "ago", "agree",
    "also", "although", "am", "among", "amount", "ancient", "angle", "angry", "animal", "announced", "another",
    "apple", "applied", "appropriate", "are", "area", "arm", "army", "around", "arrange", "arrangement", "arrive",
    "attempt", "attention", "audience", "author", "automobile", "available", "average", "avoid", "aware", "away",
    "baseball", "basic", "basis", "basket", "bat", "battle", "be", "bean", "bear", "beat", "beautiful", "beauty",
    "believed", "bell", "belong", "below", "belt", "bend", "beneath", "bent", "beside", "best", "bet", "better",
    "blanket", "blew", "blind", "block", "blood", "blow", "blue", "board", "boat", "body", "bone", "book", "border",
    "breakfast", "breath", "breathe", "breathing", "breeze", "brick", "bridge", "brief", "bright", "bring", "broad",
    "burst", "bus", "bush", "business", "busy", "but", "butter", "buy", "by", "cabin", "cage", "cake", "call", "calm",
    "care", "careful", "carefully", "carried", "carry", "case", "cast", "castle", "cat", "catch", "cattle", "caught",
    "chance", "change", "changing", "chapter", "character", "characteristic", "charge", "chart", "check", "cheese",
    "circus", "citizen", "city", "class", "classroom", "claws", "clay", "clean", "clear", "clearly", "climate", "climb",
    "coat", "coffee", "cold", "collect", "college", "colony", "color", "column", "combination", "combine", "come",
    "complex", "composed", "composition", "compound", "concerned", "condition", "congress", "connected", "consider",
    "conversation", "cook", "cookies", "cool", "copper", "copy", "corn", "corner", "correct", "correctly", "cost",
    "create", "creature", "crew", "crop", "cross", "crowd", "cry", "cup", "curious", "current", "curve", "customs",
    "dead", "deal", "dear", "death", "decide", "declared", "deep", "deeply", "deer", "definition", "degree", "depend",
    "did", "die", "differ", "difference", "different", "difficult", "difficulty", "dig", "dinner", "direct",
    "distance", "distant", "divide", "division", "do", "doctor", "does", "dog", "doing", "doll", "dollar", "done",
    "driven", "driver", "driving", "drop", "dropped", "drove", "dry", "duck", "due", "dug", "dull", "during", "dust",
    "edge", "education", "effect", "effort", "egg", "eight", "either", "electric", "electricity", "element", "elephant",
    "entirely", "environment", "equal", "equally", "equator", "equipment", "escape", "especially", "essential",
    "evidence", "exact", "exactly", "examine", "example", "excellent", "except", "exchange", "excited", "excitement",
    "express", "expression", "extra", "eye", "face", "facing", "fact", "factor", "factory", "failed", "fair", "fairly",
    "fat", "father", "favorite", "fear", "feathers", "feature", "fed", "feed", "feel", "feet", "fell", "fellow", "felt",
    "final", "finally", "find", "fine", "finest", "finger", "finish", "fire", "fireplace", "firm", "first", "fish",
    "follow", "food", "foot", "football", "for", "force", "foreign", "forest", "forget", "forgot", "forgotten", "form",
    "frequently", "fresh", "friend", "friendly", "frighten", "frog", "from", "front", "frozen", "fruit", "fuel", "full",
    "gasoline", "gate", "gather", "gave", "general", "generally", "gentle", "gently", "get", "getting", "giant", "gift",
    "got", "government", "grabbed", "grade", "gradually", "grain", "grandfather", "grandmother", "graph", "grass",
    "growth", "guard", "guess", "guide", "gulf", "gun", "habit", "had", "hair", "half", "halfway", "hall", "hand",
    "have", "having", "hay", "he", "headed", "heading", "health", "heard", "hearing", "heart", "heat", "heavy",
    "highway", "hill", "him", "himself", "his", "history", "hit", "hold", "hole", "hollow", "home", "honor", "hope",
    "hunter", "hurried", "hurry", "hurt", "husband", "ice", "idea", "identity", "if", "ill", "image", "imagine",
    "increase", "indeed", "independent", "indicate", "individual", "industrial", "industry", "influence", "information",
    "involved", "iron", "is", "island", "it", "its", "itself", "jack", "jar", "jet", "job", "join", "joined", "journey",
    "know", "knowledge", "known", "label", "labor", "lack", "lady", "laid", "lake", "lamp", "land", "language", "large",
    "least", "leather", "leave", "leaving", "led", "left", "leg", "length", "lesson", "let", "letter", "level",
    "little", "live", "living", "load", "local", "locate", "location", "log", "lonely", "long", "longer", "look",
    "machine", "machinery", "mad", "made", "magic", "magnet", "mail", "main", "mainly", "major", "make", "making",
    "material", "mathematics", "matter", "may", "maybe", "me", "meal", "mean", "means", "meant", "measure", "meat",
    "might", "mighty", "mile", "military", "milk", "mill", "mind", "mine", "minerals", "minute", "mirror", "missing",
    "moon", "more", "morning", "most", "mostly", "mother", "motion", "motor", "mountain", "mouse", "mouth", "move",
    "name", "nation", "national", "native", "natural", "naturally", "nature", "near", "nearby", "nearer", "nearest",
    "never", "new", "news", "newspaper", "next", "nice", "night", "nine", "no", "nobody", "nodded", "noise", "none",
    "object", "observe", "obtain", "occasionally", "occur", "ocean", "of", "off", "offer", "office", "officer",
    "ought", "our", "ourselves", "out", "outer", "outline", "outside", "over", "own", "owner", "oxygen", "pack",
    "part", "particles", "particular", "particularly", "partly", "parts", "party", "pass", "passage", "past", "path",
    "person", "personal", "pet", "phrase", "physical", "piano", "pick", "picture", "pictured", "pie", "piece", "pig",
    "plant", "plastic", "plate", "plates", "play", "pleasant", "please", "pleasure", "plenty", "plural", "plus",
    "popular", "population", "porch", "port", "position", "positive", "possible", "possibly", "post", "pot", "potatoes",
    "pressure", "pretty", "prevent", "previous", "price", "pride", "primitive", "principal", "principle", "printed",
    "promised", "proper", "properly", "property", "protection", "proud", "prove", "provide", "public", "pull", "pupil",
    "quietly", "quite", "rabbit", "race", "radio", "railroad", "rain", "raise", "ran", "ranch", "range", "rapidly",
    "recent", "recently", "recognize", "record", "red", "refer", "refused", "region", "regular", "related",
    "require", "research", "respect", "rest", "result", "return", "review", "rhyme", "rhythm", "rice", "rich", "ride",
    "room", "root", "rope", "rose", "rough", "round", "route", "row", "rubbed", "rubber", "rule", "ruler", "run",
    "satellites", "satisfied", "save", "saved", "saw", "say", "scale", "scared", "scene", "school", "science",
    "seeing", "seems", "seen", "seldom", "select", "selection", "sell", "send", "sense", "sent", "sentence", "separate",
    "shake", "shaking", "shall", "shallow", "shape", "share", "sharp", "she", "sheep", "sheet", "shelf", "shells",
    "shoulder", "shout", "show", "shown", "shut", "sick", "sides", "sight", "sign", "signal", "silence", "silent",
    "sitting", "situation", "six", "size", "skill", "skin", "sky", "slabs", "slave", "sleep", "slept", "slide",
    "smooth", "snake", "snow", "so", "soap", "social", "society", "soft", "softly", "soil", "solar", "sold", "soldier",
    "song", "soon", "sort", "sound", "source", "south", "southern", "space", "speak", "special", "species", "specific",
    "spring", "square", "stage", "stairs", "stand", "standard", "star", "stared", "start", "state", "statement",
    "stone", "stood", "stop", "stopped", "store", "storm", "story", "stove", "straight", "strange", "stranger", "straw",
    "struggle", "stuck", "student", "studied", "studying", "subject", "substance", "success", "successful", "such",
    "suppose", "sure", "surface", "surprise", "surrounded", "swam", "sweet", "swept", "swim", "swimming", "swing",
    "taste", "taught", "tax", "tea", "teach", "teacher", "team", "tears", "teeth", "telephone", "television", "tell",
    "theory", "there", "therefore", "these", "they", "thick", "thin", "thing", "think", "third", "thirty", "this",
    "thrown", "thumb", "thus", "thy", "tide", "tie", "tight", "tightly", "till", "time", "tin", "tiny", "tip", "tired",
    "top", "topic", "torn", "total", "touch", "toward", "tower", "town", "toy", "trace", "track", "trade", "traffic",
    "troops", "tropical", "trouble", "truck", "trunk", "truth", "try", "tube", "tune", "turn", "twelve", "twenty",
    "unknown", "unless", "until", "unusual", "up", "upon", "upper", "upward", "us", "use", "useful", "using", "usual",
    "very", "vessels", "victory", "view", "village", "visit", "visitor", "voice", "volume", "vote", "vowel", "voyage",
    "we", "weak", "wealth", "wear", "weather", "week", "weigh", "weight", "welcome", "well", "went", "were", "west",
    "which", "while", "whispered", "whistle", "white", "who", "whole", "whom", "whose", "why", "wide", "widely", "wife",
    "without", "wolf", "women", "won", "wonder", "wonderful", "wood", "wooden", "wool", "word", "wore", "work",
    "wrote", "yard", "year", "yellow", "yes", "yesterday", "yet", "you", "young", "younger", "your", "yourself",
)


def create_fake_title(i):
    words = []
    for j in range(1, random.randrange(4, 8)):
        words.append(WORDLIST[random.randint(0, len(WORDLIST)-1)])
    return " ".join(words)


def create_fake_articles(apps, schema_editor):
    """
    Create a random list of articles of sufficient size to test the workings and performance of the module.  Each
    article will have it's information set to something approaching a possible use-case.
    """
    Article = apps.get_model("articles", "Article")

    for i in range(1, 10000):
        Article.objects.create(
            title=create_fake_title(i),
            posted=timezone.now() - timedelta(minutes=i*10 + random.randint(1, 60)),
            upvotes=max(0, int(random.gauss(10, 30))),    # Gaussian distribution centered at 10, standard
            downvotes=max(0, int(random.gauss(10, 30))),  # deviation of 30, throw away negative results
        )


def delete_fake_articles(apps, schema_editor):
    Article = apps.get_model("articles", "Article")

    Article.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_fake_articles, delete_fake_articles),
    ]
