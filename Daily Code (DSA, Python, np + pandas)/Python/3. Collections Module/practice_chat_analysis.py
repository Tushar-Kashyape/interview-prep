"""
You're processing a stream of chat messages, each represented as (username, message)
tuples. Build a function that:

Counts how many messages each user sent (Counter)
Groups all messages by username (defaultdict)
Returns the 3 most active users and their message count
"""
from collections import Counter, defaultdict


def analyze_chat(messages: list[tuple[str, str]]):
    msg_counter = Counter(msg[0] for msg in messages)
    top_3 = msg_counter.most_common(3)

    msg_dd = defaultdict(list)
    for msg in messages:
        msg_dd[msg[0]].append(msg[1])

    return top_3, msg_dd


messages = [("alice", "hi"), ("bob", "hey"), ("alice", "how are you"),("charlie", "yo"),
            ("alice", "great thanks"), ("bob", "good"), ("dave", "sup"), ("alice", "bye"),
            ("charlie", "later")]

top_users, grouped_messages = analyze_chat(messages)
print(top_users)
print(grouped_messages)

"""
Logged: 

collections | analyze_chat (Counter + defaultdict combined) | Correct, first try, cold |
Articulation: strong — both follow-ups answered correctly with good cross-topic 
connections (laziness from Generators, stability from Lambdas) | Referred: no | 
Insight: good synthesis across previously-covered topics, exactly the "combined problem" 
goal for this module.
"""