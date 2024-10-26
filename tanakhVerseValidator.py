#src/validator/bible_verse_validator.py

# Define the data structure for the Tanakh
tanakh = [
    {"book_number": 1, "name": "Genesis", "chapters": [
        31, 25, 24, 26, 32, 22, 24, 22, 29, 32,
        32, 20, 18, 24, 21, 16, 27, 33, 38, 18,
        34, 24, 20, 67, 34, 35, 46, 22, 35, 43,
        54, 33, 20, 31, 29, 43, 36, 30, 23, 23,
        57, 38, 34, 34, 28, 34, 31, 22, 33, 26
    ]},
    {"book_number": 2, "name": "Exodus", "chapters": [
        22, 25, 22, 31, 23, 30, 29, 28, 35, 29,
        10, 51, 22, 31, 27, 36, 16, 27, 25, 22,
        37, 30, 33, 18, 40, 37, 21, 43, 46, 38,
        18, 35, 23, 35, 35, 38, 29, 31, 43, 38
    ]},
    {"book_number": 3, "name": "Leviticus", "chapters": [
        17, 16, 17, 35, 26, 23, 38, 36, 24, 20,
        47, 8, 59, 57, 33, 34, 16, 30, 37, 27,
        24, 33, 44, 23, 55, 46, 34
    ]},
    {"book_number": 4, "name": "Numbers", "chapters": [
        54, 34, 51, 49, 31, 27, 89, 26, 23, 36,
        35, 16, 33, 45, 41, 35, 28, 32, 22, 29,
        35, 41, 30, 25, 18, 65, 23, 31, 39, 17,
        54, 42, 56, 29, 34, 13
    ]},
    {"book_number": 5, "name": "Deuteronomy", "chapters": [
        46, 37, 29, 49, 29, 25, 26, 20, 29, 22,
        32, 31, 19, 29, 23, 22, 20, 22, 21, 20,
        23, 29, 26, 22, 19, 19, 26, 69, 28, 20,
        30, 52, 29, 12
    ]},
    {"book_number": 6, "name": "Joshua", "chapters": [
        18, 24, 17, 24, 15, 27, 26, 35, 27, 43,
        23, 24, 33, 15, 63, 10, 18, 28, 51, 9,
        43, 34, 16, 33
    ]},
    {"book_number": 7, "name": "Judges", "chapters": [
        36, 23, 31, 24, 31, 40, 25, 35, 57, 18,
        40, 15, 25, 20, 20, 31, 13, 31, 30, 48,
        25
    ]},
    {"book_number": 8, "name": "Ruth", "chapters": [22, 23, 18, 22]},
    {"book_number": 9, "name": "1 Samuel", "chapters": [
        28, 36, 21, 22, 12, 21, 17, 22, 27, 27,
        15, 25, 23, 52, 35, 23, 58, 30, 24, 42,
        16, 23, 29, 22, 44, 25, 12, 25, 11, 31,
        13
    ]},
    {"book_number": 10, "name": "2 Samuel", "chapters": [
        27, 32, 39, 12, 25, 23, 29, 18, 13, 19,
        27, 31, 39, 33, 37, 23, 29, 32, 44, 26,
        22, 51, 39, 25
    ]},
    {"book_number": 11, "name": "1 Kings", "chapters": [
        53, 46, 28, 20, 32, 38, 51, 66, 28, 29,
        43, 33, 34, 31, 34, 34, 24, 46, 21, 43,
        29, 54
    ]},
    {"book_number": 12, "name": "2 Kings", "chapters": [
        18, 25, 27, 44, 27, 33, 20, 29, 37, 36,
        20, 22, 25, 29, 38, 20, 41, 37, 37, 21,
        26, 20, 37, 20, 30
    ]},
    {"book_number": 13, "name": "1 Chronicles", "chapters": [
        54, 55, 24, 43, 41, 66, 40, 40, 44, 14,
        47, 41, 14, 17, 29, 43, 27, 17, 19, 8,
        30, 19, 32, 31, 31, 32, 34, 21, 30
    ]},
    {"book_number": 14, "name": "2 Chronicles", "chapters": [
        18, 17, 17, 22, 14, 42, 22, 18, 31, 19,
        23, 16, 23, 14, 19, 14, 19, 34, 11, 37,
        20, 12, 21, 27, 28, 23, 9, 27, 36, 27,
        21, 33, 25, 33, 27, 23
    ]},
    {"book_number": 15, "name": "Ezra", "chapters": [11, 70, 13, 24, 17, 22, 28, 36, 15, 44]},
    {"book_number": 16, "name": "Nehemiah", "chapters": [
        11, 20, 38, 17, 19, 19, 72, 18, 37, 40,
        36, 47, 31
    ]},
    {"book_number": 17, "name": "Esther", "chapters": [22, 23, 15, 17, 14, 14, 10, 17, 32, 3]},
    {"book_number": 18, "name": "Job", "chapters": [
        22, 13, 26, 21, 27, 30, 21, 22, 35, 22,
        20, 25, 28, 22, 35, 22, 16, 21, 29, 29,
        34, 30, 17, 25, 6, 14, 23, 28, 25, 31,
        40, 22, 33, 37, 16, 33, 24, 41, 30, 32,
        26, 17
    ]},
    {"book_number": 19, "name": "Psalms", "chapters": [
        6, 12, 9, 9, 13, 11, 18, 10, 21, 18,
        7, 9, 6, 7, 5, 11, 15, 51, 15, 10,
        14, 32, 6, 10, 22, 12, 14, 9, 11, 13,
        25, 11, 22, 23, 28, 13, 40, 23, 14, 18,
        14, 12, 5, 27, 18, 12, 10, 15, 21, 23,
        21, 11, 7, 9, 24, 14, 12, 12, 18, 14,
        9, 13, 12, 11, 14, 20, 8, 36, 37, 5,
        24, 20, 28, 23, 11, 13, 21, 72, 13, 20,
        17, 8, 19, 13, 14, 17, 7, 19, 53, 17,
        16, 16, 5, 23, 11, 13, 12, 9, 9, 5,
        8, 29, 22, 35, 45, 48, 43, 13, 31, 7,
        10, 10, 9, 8, 18, 19, 2, 29, 176, 7,
        8, 9, 4, 8, 5, 6, 5, 6, 8, 8,
        3, 18, 3, 3, 21, 26, 9, 8, 24, 14,
        10, 8, 12, 15, 21, 10, 20, 14, 9, 6
    ]},
    {"book_number": 20, "name": "Proverbs", "chapters": [
        33, 22, 35, 27, 23, 35, 27, 36, 18, 32,
        31, 28, 25, 35, 33, 33, 28, 24, 29, 30,
        31, 29, 35, 34, 28, 28, 27, 28, 27, 33, 31
    ]},
    {"book_number": 21, "name": "Ecclesiastes", "chapters": [
        18, 26, 22, 17, 19, 12, 29, 17, 18, 20,
        10, 14
    ]},
    {"book_number": 22, "name": "Song of Songs", "chapters": [
        17, 17, 11, 16, 16, 12, 14, 14
    ]},
    {"book_number": 23, "name": "Isaiah", "chapters": [
        31, 22, 26, 6, 30, 13, 25, 23, 20, 34,
        16, 6, 22, 32, 9, 14, 14, 7, 25, 6,
        17, 25, 18, 23, 12, 21, 13, 29, 24, 33,
        9, 20, 24, 17, 10, 22, 38, 22, 8, 31,
        29, 25, 28, 28, 25, 13, 15, 22, 26, 11,
        23, 15, 12, 17, 13, 12, 21, 14, 21, 22,
        11, 12, 19, 11, 25, 24
    ]},
    {"book_number": 24, "name": "Jeremiah", "chapters": [
        19, 37, 25, 31, 31, 30, 34, 23, 25, 25,
        23, 17, 27, 22, 21, 21, 27, 23, 15, 18,
        14, 30, 40, 10, 38, 24, 22, 17, 32, 25,
        39, 44, 26, 22, 19, 32, 21, 28, 18, 16,
        18, 22, 13, 30, 5, 28, 7, 47, 39, 46,
        64, 34
    ]},
    {"book_number": 25, "name": "Lamentations", "chapters": [22, 22, 66, 22, 22]},
    {"book_number": 26, "name": "Ezekiel", "chapters": [
        28, 10, 27, 17, 17, 14, 27, 18, 11, 22,
        25, 28, 23, 23, 8, 63, 24, 32, 14, 44,
        37, 31, 49, 27, 17, 21, 36, 26, 21, 26,
        18, 32, 33, 31, 15, 38, 28, 23, 29, 49,
        26, 20, 27, 31, 25, 24, 23, 35
    ]},
    {"book_number": 27, "name": "Daniel", "chapters": [
        21, 49, 33, 34, 30, 29, 28, 27, 27, 21,
        45, 13
    ]},
    {"book_number": 28, "name": "Hosea", "chapters": [
        9, 25, 5, 19, 15, 11, 16, 14, 17, 15,
        11, 15, 15, 10
    ]},
    {"book_number": 29, "name": "Joel", "chapters": [
        20, 27, 5, 21
    ]},
    {"book_number": 30, "name": "Amos", "chapters": [
        15, 16, 15, 13, 27, 14, 17, 14, 15
    ]},
    {"book_number": 31, "name": "Obadiah", "chapters": [21]},
    {"book_number": 32, "name": "Jonah", "chapters": [16, 11, 10, 11]},
    {"book_number": 33, "name": "Micah", "chapters": [
        16, 13, 12, 14, 14, 16, 20
    ]},
    {"book_number": 34, "name": "Nahum", "chapters": [14, 14, 19]},
    {"book_number": 35, "name": "Habakkuk", "chapters": [17, 20, 19]},
    {"book_number": 36, "name": "Zephaniah", "chapters": [18, 15, 20]},
    {"book_number": 37, "name": "Haggai", "chapters": [15, 23]},
    {"book_number": 38, "name": "Zechariah", "chapters": [
        17, 17, 10, 14, 11, 15, 14, 23, 17, 12,
        17, 14, 9, 21
    ]},
    {"book_number": 39, "name": "Malachi", "chapters": [14, 17, 24, 6]}
]

# Define the data structure for the KJV Bible
bible_kjv = [
    {"book_number": 1, "name": "Genesis", "chapters": [
        31, 25, 24, 26, 32, 22, 24, 22, 29, 32,
        32, 20, 18, 24, 21, 16, 27, 33, 38, 18,
        34, 24, 20, 67, 34, 35, 46, 22, 35, 43,
        55, 32, 20, 31, 29, 43, 36, 30, 23, 23,
        57, 38, 34, 34, 28, 34, 31, 22, 33, 26
    ]},
    {"book_number": 2, "name": "Exodus", "chapters": [
        22, 25, 22, 31, 23, 30, 25, 32, 35, 29,
        10, 51, 22, 31, 27, 36, 16, 27, 25, 26,
        36, 31, 33, 18, 40, 37, 21, 43, 46, 38,
        18, 35, 23, 35, 35, 38, 29, 31, 43, 38
    ]},
    {"book_number": 3, "name": "Leviticus", "chapters": [
        17, 16, 17, 35, 19, 30, 38, 36, 24, 20,
        47, 8, 59, 57, 33, 34, 16, 30, 37, 27,
        24, 33, 44, 23, 55, 46, 34
    ]},
    {"book_number": 4, "name": "Numbers", "chapters": [
        54, 34, 51, 49, 31, 27, 89, 26, 23, 36,
        35, 16, 33, 45, 41, 50, 13, 32, 22, 29,
        35, 41, 30, 25, 18, 65, 23, 31, 40, 16,
        54, 42, 56, 29, 34, 13
    ]},
    {"book_number": 5, "name": "Deuteronomy", "chapters": [
        46, 37, 29, 49, 33, 25, 26, 20, 29, 22,
        32, 32, 18, 29, 23, 22, 20, 22, 21, 20,
        23, 30, 25, 22, 19, 19, 26, 68, 29, 20,
        30, 52, 29, 12
    ]},
    {"book_number": 6, "name": "Joshua", "chapters": [
        18, 24, 17, 24, 15, 27, 26, 35, 27, 43,
        23, 24, 33, 15, 63, 10, 18, 28, 51, 9,
        45, 34, 16, 33
    ]},
    {"book_number": 7, "name": "Judges", "chapters": [
        36, 23, 31, 24, 31, 40, 25, 35, 57, 18,
        40, 15, 25, 20, 20, 31, 13, 31, 30, 48,
        25
    ]},
    {"book_number": 8, "name": "Ruth", "chapters": [22, 23, 18, 22]},
    {"book_number": 9, "name": "1 Samuel", "chapters": [
        28, 36, 21, 22, 12, 21, 17, 22, 27, 27,
        15, 25, 23, 52, 35, 23, 58, 30, 24, 42,
        15, 23, 29, 22, 44, 25, 12, 25, 11, 31,
        13
    ]},
    {"book_number": 10, "name": "2 Samuel", "chapters": [
        27, 32, 39, 12, 25, 23, 29, 18, 13, 19,
        27, 31, 39, 33, 37, 23, 29, 33, 43, 26,
        22, 51, 39, 25
    ]},
    {"book_number": 11, "name": "1 Kings", "chapters": [
        53, 46, 28, 34, 18, 38, 51, 66, 28, 29,
        43, 33, 34, 31, 34, 34, 24, 46, 21, 43,
        29, 53
    ]},
    {"book_number": 12, "name": "2 Kings", "chapters": [
        18, 25, 27, 44, 27, 33, 20, 29, 37, 36,
        21, 21, 25, 29, 38, 20, 41, 37, 37, 21,
        26, 20, 37, 20, 30
    ]},
    {"book_number": 13, "name": "1 Chronicles", "chapters": [
        54, 55, 24, 43, 26, 81, 40, 40, 44, 14,
        47, 40, 14, 17, 29, 43, 27, 17, 19, 8,
        30, 19, 32, 31, 31, 32, 34, 21, 30
    ]},
    {"book_number": 14, "name": "2 Chronicles", "chapters": [
        17, 18, 17, 22, 14, 42, 22, 18, 31, 19,
        23, 16, 22, 15, 19, 14, 19, 34, 11, 37,
        20, 12, 21, 27, 28, 23, 9, 27, 36, 27,
        21, 33, 25, 33, 27, 23
    ]},
    {"book_number": 15, "name": "Ezra", "chapters": [11, 70, 13, 24, 17, 22, 28, 36, 15, 44]},
    {"book_number": 16, "name": "Nehemiah", "chapters": [
        11, 20, 32, 23, 19, 19, 73, 18, 38, 39,
        36, 47, 31
    ]},
    {"book_number": 17, "name": "Esther", "chapters": [22, 23, 15, 17, 14, 14, 10, 17, 32, 3]},
    {"book_number": 18, "name": "Job", "chapters": [
        22, 13, 26, 21, 27, 30, 21, 22, 35, 22,
        20, 25, 28, 22, 35, 22, 16, 21, 29, 29,
        34, 30, 17, 25, 6, 14, 23, 28, 25, 31,
        40, 22, 33, 37, 16, 33, 24, 41, 30, 24,
        34, 17
    ]},
    {"book_number": 19, "name": "Psalms", "chapters": [
        6, 12, 8, 8, 12, 10, 17, 9, 20, 18,
        7, 8, 6, 7, 5, 11, 15, 50, 14, 9,
        13, 31, 6, 10, 22, 12, 14, 9, 11, 12,
        24, 11, 22, 22, 28, 12, 40, 22, 13, 17,
        13, 11, 5, 26, 17, 11, 9, 14, 20, 23,
        19, 9, 6, 7, 23, 13, 11, 11, 17, 12,
        8, 12, 11, 10, 13, 20, 7, 35, 36, 5,
        24, 20, 28, 23, 10, 12, 20, 72, 13, 19,
        16, 8, 18, 12, 13, 17, 7, 18, 52, 17,
        16, 15, 5, 23, 11, 13, 12, 9, 9, 5,
        8, 28, 22, 35, 45, 48, 43, 13, 31, 7,
        10, 10, 9, 8, 18, 19, 2, 29, 176, 7,
        8, 9, 4, 8, 5, 6, 5, 6, 8, 8,
        3, 18, 3, 3, 21, 26, 9, 8, 24, 13,
        10, 7, 12, 15, 21, 10, 20, 14, 9, 6
    ]},
    {"book_number": 20, "name": "Proverbs", "chapters": [
        33, 22, 35, 27, 23, 35, 27, 36, 18, 32,
        31, 28, 25, 35, 33, 33, 28, 24, 29, 30,
        31, 29, 35, 34, 28, 28, 27, 28, 27, 33, 31
    ]},
    {"book_number": 21, "name": "Ecclesiastes", "chapters": [
        18, 26, 22, 16, 20, 12, 29, 17, 18, 20,
        10, 14
    ]},
    {"book_number": 22, "name": "Song of Solomon", "chapters": [17, 17, 11, 16, 16, 13, 13, 14]},
    {"book_number": 23, "name": "Isaiah", "chapters": [
        31, 22, 26, 6, 30, 13, 25, 22, 21, 34,
        16, 6, 22, 32, 9, 14, 14, 7, 25, 6,
        17, 25, 18, 23, 12, 21, 13, 29, 24, 33,
        9, 20, 24, 17, 10, 22, 38, 22, 8, 31,
        29, 25, 28, 28, 25, 13, 15, 22, 26, 11,
        23, 15, 12, 17, 13, 12, 21, 14, 21, 22,
        11, 12, 19, 12, 25, 24
    ]},
    {"book_number": 24, "name": "Jeremiah", "chapters": [
        19, 37, 25, 31, 31, 30, 34, 22, 26, 25,
        23, 17, 27, 22, 21, 21, 27, 23, 15, 18,
        14, 30, 40, 10, 38, 24, 22, 17, 32, 24,
        40, 44, 26, 22, 19, 32, 21, 28, 18, 16,
        18, 22, 13, 30, 5, 28, 7, 47, 39, 46,
        64, 34
    ]},
    {"book_number": 25, "name": "Lamentations", "chapters": [22, 22, 66, 22, 22]},
    {"book_number": 26, "name": "Ezekiel", "chapters": [
        28, 10, 27, 17, 17, 14, 27, 18, 11, 22,
        25, 28, 23, 23, 8, 63, 24, 32, 14, 49,
        32, 31, 49, 27, 17, 21, 36, 26, 21, 26,
        18, 32, 33, 31, 15, 38, 28, 23, 29, 49,
        26, 20, 27, 31, 25, 24, 23, 35
    ]},
    {"book_number": 27, "name": "Daniel", "chapters": [
        21, 49, 30, 37, 31, 28, 28, 27, 27, 21,
        45, 13
    ]},
    {"book_number": 28, "name": "Hosea", "chapters": [
        11, 23, 5, 19, 15, 11, 16, 14, 17, 15,
        12, 14, 16, 9
    ]},
    {"book_number": 29, "name": "Joel", "chapters": [20, 32, 21]},
    {"book_number": 30, "name": "Amos", "chapters": [
        15, 16, 15, 13, 27, 14, 17, 14, 15
    ]},
    {"book_number": 31, "name": "Obadiah", "chapters": [21]},
    {"book_number": 32, "name": "Jonah", "chapters": [17, 10, 10, 11]},
    {"book_number": 33, "name": "Micah", "chapters": [
        16, 13, 12, 13, 15, 16, 20
    ]},
    {"book_number": 34, "name": "Nahum", "chapters": [15, 13, 19]},
    {"book_number": 35, "name": "Habakkuk", "chapters": [17, 20, 19]},
    {"book_number": 36, "name": "Zephaniah", "chapters": [18, 15, 20]},
    {"book_number": 37, "name": "Haggai", "chapters": [15, 23]},
    {"book_number": 38, "name": "Zechariah", "chapters": [
        21, 13, 10, 14, 11, 15, 14, 23, 17, 12,
        17, 14, 9, 21
    ]},
    {"book_number": 39, "name": "Malachi", "chapters": [14, 17, 18, 6]},
    {"book_number": 40, "name": "Matthew", "chapters": [
        25, 23, 17, 25, 48, 34, 29, 34, 38, 42,
        30, 50, 58, 36, 39, 28, 27, 35, 30, 34,
        46, 46, 39, 51, 46, 75, 66, 20
    ]},
    {"book_number": 41, "name": "Mark", "chapters": [
        45, 28, 35, 41, 43, 56, 37, 38, 50, 52,
        33, 44, 37, 72, 47, 20
    ]},
    {"book_number": 42, "name": "Luke", "chapters": [
        80, 52, 38, 44, 39, 49, 50, 56, 62, 42,
        54, 59, 35, 35, 32, 31, 37, 43, 48, 47,
        38, 71, 56, 53
    ]},
    {"book_number": 43, "name": "John", "chapters": [
        51, 25, 36, 54, 47, 71, 53, 59, 41, 42,
        57, 50, 38, 31, 27, 33, 26, 40, 42, 31,
        25
    ]},
    {"book_number": 44, "name": "Acts", "chapters": [
        26, 47, 26, 37, 42, 15, 60, 40, 43, 48,
        30, 25, 52, 28, 41, 40, 34, 28, 41, 38,
        40, 30, 35, 27, 27, 32, 44, 31
    ]},
    {"book_number": 45, "name": "Romans", "chapters": [
        32, 29, 31, 25, 21, 23, 25, 39, 33, 21,
        36, 21, 14, 23, 33, 27
    ]},
    {"book_number": 46, "name": "1 Corinthians", "chapters": [
        31, 16, 23, 21, 13, 20, 40, 13, 27, 33,
        34, 31, 13, 40, 58, 24
    ]},
    {"book_number": 47, "name": "2 Corinthians", "chapters": [
        24, 17, 18, 18, 21, 18, 16, 24, 15, 18,
        33, 21, 14
    ]},
    {"book_number": 48, "name": "Galatians", "chapters": [24, 21, 29, 31, 26, 18]},
    {"book_number": 49, "name": "Ephesians", "chapters": [23, 22, 21, 32, 33, 24]},
    {"book_number": 50, "name": "Philippians", "chapters": [30, 30, 21, 23]},
    {"book_number": 51, "name": "Colossians", "chapters": [29, 23, 25, 18]},
    {"book_number": 52, "name": "1 Thessalonians", "chapters": [10, 20, 13, 18, 28]},
    {"book_number": 53, "name": "2 Thessalonians", "chapters": [12, 17, 18]},
    {"book_number": 54, "name": "1 Timothy", "chapters": [20, 15, 16, 16, 25, 21]},
    {"book_number": 55, "name": "2 Timothy", "chapters": [18, 26, 17, 22]},
    {"book_number": 56, "name": "Titus", "chapters": [16, 15, 15]},
    {"book_number": 57, "name": "Philemon", "chapters": [25]},
    {"book_number": 58, "name": "Hebrews", "chapters": [
        14, 18, 19, 16, 14, 20, 28, 13, 28, 39,
        40, 29, 25
    ]},
    {"book_number": 59, "name": "James", "chapters": [27, 26, 18, 17, 20]},
    {"book_number": 60, "name": "1 Peter", "chapters": [25, 25, 22, 19, 14]},
    {"book_number": 61, "name": "2 Peter", "chapters": [21, 22, 18]},
    {"book_number": 62, "name": "1 John", "chapters": [10, 29, 24, 21, 21]},
    {"book_number": 63, "name": "2 John", "chapters": [13]},
    {"book_number": 64, "name": "3 John", "chapters": [14]},
    {"book_number": 65, "name": "Jude", "chapters": [25]},
    {"book_number": 66, "name": "Revelation", "chapters": [
        20, 29, 22, 11, 14, 17, 17, 13, 21, 11,
        19, 17, 18, 20, 8, 21, 18, 24, 21, 15,
        27, 21
    ]}
]

# Function to validate the total verses
def validate_verses(book_name: str, chapter_number: int, total_verses: int) -> bool:
    # Find the book by book_name
    book = next((b for b in tanakh if b["name"] == book_name), None)
    if not book:
        print(f"Book number {book_name} is invalid. There are only {len(tanakh)} books.")
        return False

    # Check if chapter_number is valid
    if chapter_number < 1 or chapter_number > len(book["chapters"]):
        print(f"Chapter number {chapter_number} is invalid for {book['name']}. It has {len(book['chapters'])} chapters.")
        return False

    # Get the actual number of verses
    actual_verses = book["chapters"][chapter_number - 1]

    # Validate the total verses
    if total_verses == actual_verses:
        #print(f"Correct! {book['name']} Chapter {chapter_number} has {actual_verses} verses.")
        return True
    else:
        print(f"Incorrect. {book['name']} Chapter {chapter_number} must have {total_verses} verses in tanakh python variable.")
        return False

# # Example usage:
# validate_verses(1, 1, 31)   # Should print that it's correct
# validate_verses(19, 119, 176)  # Should print that it's correct (Psalm 119)
# validate_verses(1, 1, 30)   # Should print the correct number of verses
# validate_verses(2, 20, 15)  # Should print the correct number of verses


def compare_bible_versions():
    """
    Compare chapter verse counts between Tanakh and KJV Bible versions.
    Returns a list of discrepancies found.
    """
    discrepancies = []
    
    # Since Tanakh only contains Old Testament books, we'll limit comparison to first 39 books
    for tanakh_book in tanakh:
        book_number = tanakh_book["book_number"]
        # Find corresponding KJV book
        kjv_book = next((book for book in bible_kjv if book["book_number"] == book_number), None)
        
        if kjv_book:
            # Compare chapter counts
            if len(tanakh_book["chapters"]) != len(kjv_book["chapters"]):
                discrepancies.append({
                    "book": tanakh_book["name"],
                    "issue": "Chapter count mismatch",
                    "tanakh_chapters": len(tanakh_book["chapters"]),
                    "kjv_chapters": len(kjv_book["chapters"])
                })
            
            # Compare verse counts within each chapter
            for chapter_num, (tanakh_verses, kjv_verses) in enumerate(zip(tanakh_book["chapters"], kjv_book["chapters"]), 1):
                if tanakh_verses != kjv_verses:
                    discrepancies.append({
                        "book": tanakh_book["name"],
                        "chapter": chapter_num,
                        "issue": "Verse count mismatch",
                        "tanakh_verses": tanakh_verses,
                        "kjv_verses": kjv_verses
                    })
            
            # Check for name differences
            if tanakh_book["name"] != kjv_book["name"]:
                discrepancies.append({
                    "book": f"{tanakh_book['name']} / {kjv_book['name']}",
                    "issue": "Book name difference",
                    "tanakh_name": tanakh_book["name"],
                    "kjv_name": kjv_book["name"]
                })
    
    return discrepancies

# Usage example:
# discrepancies = compare_bible_versions(tanakh, bible_kjv)
# for d in discrepancies:
#     print(f"\nIssue found in {d['book']}:")
#     for key, value in d.items():
#         if key != 'book':
#             print(f"  {key}: {value}")