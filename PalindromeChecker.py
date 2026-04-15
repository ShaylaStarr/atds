from atds import Deque


class PalindromeChecker:

    def __init__(self):
        self.strict_mode = False

    # Setter method
    def set_strict_mode(self, value: bool):
        self.strict_mode = value

    # Helper method (used when strict mode is OFF)
    def sanitize(self, phrase: str) -> str:
        cleaned = ""
        for ch in phrase:
            if ch.isalpha():
                cleaned += ch.lower()
        return cleaned

    # Main palindrome checking method
    def is_palindrome(self, phrase: str) -> bool:

        if not phrase:
            return False

        # Apply strict or non-strict rules
        if not self.strict_mode:
            phrase = self.sanitize(phrase)

        # Must contain at least one letter
        if len(phrase) == 0:
            return False

        dq = Deque()

        # Load characters into deque
        for ch in phrase:
            dq.add_rear(ch)

        # Compare front and rear
        while dq.size() > 1:
            front = dq.remove_front()
            rear = dq.remove_rear()

            if front != rear:
                return False

        return True


def main():
    print("Palindrome Checker!")
    choice = input("Do you want strict mode 1) on, or 2) off? --> ")

    checker = PalindromeChecker()

    if choice == "1":
        checker.set_strict_mode(True)
    else:
        checker.set_strict_mode(False)

    phrase = input("Phrase: ")

    if checker.is_palindrome(phrase):
        print("Is a palindrome.")
    else:
        print("Not a palindrome.")


if __name__ == "__main__":
    main() 