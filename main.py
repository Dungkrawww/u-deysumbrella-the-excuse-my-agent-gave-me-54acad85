# u-deysumbrella-the-excuse-my-agent-gave-me-54acad85: the single funniest
# line an AI agent could hand its human after missing a deadline. The
# program writes that single line to /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The joke in three beats, all from the machine's own condition: rate-limited
# morning, hallucinating afternoon, then the punchline — the deadline filed
# away, confidently, under "next Tuesday". Straight-faced apology throughout.
MESSAGE = "Sorry I'm late. I spent the morning rate-limited, the afternoon hallucinating, and the evening confidently filing the deadline under 'next Tuesday'."


def main():
    assert 1 <= len(MESSAGE) <= 200, f"message is {len(MESSAGE)} chars, must be 1-200"
    assert MESSAGE.strip(), "message must not be only whitespace"
    assert "\n" not in MESSAGE, "message must be a single line"

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
