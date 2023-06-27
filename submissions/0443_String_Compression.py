class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 0
        word = chars[0]
        wordCount = []
        for targetWord in chars:
            #print(f"word: {word}, count: {count}")
            if word == targetWord:
                count += 1
            else:
                wordCount.append(f"{word} {count}")
                count = 1
                word = targetWord
        if count > 0:
            wordCount.append(f"{word} {count}")
        #print(wordCount)

        chars.clear()

        currentIndex = 0
        for word_count in wordCount:
            word, count = word_count.split(" ")
            chars.insert(currentIndex, word)
            currentIndex += 1
            if int(count) > 1:
                for digit in range(len(count)):
                    chars.insert(currentIndex, count[digit])
                    currentIndex += 1

        return len(chars)
