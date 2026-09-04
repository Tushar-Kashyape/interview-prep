"""
Build a small file-processing system with a custom exception hierarchy:

. FileProcessingError — base exception, no extra attributes
. FileFormatError(FileProcessingError) — raised when content isn't a valid number;
stores the bad content as .content
. FileEmptyError(FileProcessingError) — raised when content is an empty string

Write process_file(content):

. If content is empty (""), raise FileEmptyError
. Try converting content to an int; if it fails, raise FileFormatError (chained from
the original error) with the bad content stored
. If successful, return the doubled value

Then write handling code that:

Catches FileFormatError specifically first (different message, mentions the bad content)
Catches FileEmptyError specifically next (different message)
Catches FileProcessingError as a fallback for any other case in this hierarchy
Logs (just print) and re-raises if it's genuinely unexpected (any other exception type)
"""
class FileProcessingError(Exception):
    pass

class FileFormatError(FileProcessingError):
    def __init__(self, content):
        super().__init__(f"Cannot process file {content}")
        self.content = content

class FileEmptyError(FileProcessingError):
    pass


def process_file(content):
    if not content or content == "":
        raise FileEmptyError()

    try:
        result = int(content) * 2
    except ValueError as e:
        raise FileFormatError(content) from e
    else:
        return result

data = ["42", "", "content"]

for content in data:
    try:
        print(process_file(content))
    except FileEmptyError as e:
        print(f"File is empty")
    except FileFormatError as e:
        print(f"Format error with content '{e.content}'")
    except FileProcessingError as e:
        print(f"General File Processing Error")
    except Exception as e:
        print(f"Unexpected error, re-raise")
        raise

"""
Logged:

Exceptions | Problem #4 (custom hierarchy + multi-except ordering + re-raise, 
checkpointed) | Correct across all checkpoints, one initial jump-ahead misstep 
(skipped straight to a broken process_file before hierarchy was solid, self-corrected 
once flagged) | Articulation: correct on ordering rule; asked a genuinely sharp 
follow-up question distinguishing sibling-ordering (arbitrary) from parent-child-ordering 
(mandatory) | Referred: minor guidance on try/except placement | 
Insight: strong overall — the sibling-vs-parent ordering question shows real analytical 
thinking beyond just pattern-matching the rule.
"""

