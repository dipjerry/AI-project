import re
import sys
def detect_programming_language(file_name):
    file_extension = file_name.split('.')[-1].lower()
    if file_extension == 'py':
        return 'Python'
    elif file_extension == 'java':
        return 'Java'
    elif file_extension == 'cpp' or file_extension == 'cxx':
        return 'C++'
    elif file_extension == 'c':
        return 'C'
    elif file_extension == 'html' or file_extension == 'htm':
        return 'HTML'
    elif file_extension == 'css':
        return 'CSS'
    elif file_extension == 'js':
        return 'JavaScript'
    elif file_extension == 'php':
        return 'PHP'
    elif file_extension == 'rb':
        return 'Ruby'
    elif file_extension == 'pl':
        return 'Perl'
    elif file_extension == 'swift':
        return 'Swift'
    elif file_extension == 'go':
        return 'Go'
    elif file_extension == 'rs':
        return 'Rust'
    elif file_extension == 'ts':
        return 'TypeScript'
    elif file_extension == 'sh':
        return 'Shell'
    elif file_extension == 'sql':
        return 'SQL'
    elif file_extension == 'pro':
        return 'Prolog'
    else:
        try:
            with open(file_name, 'r') as file:
                code_segment = file.read()
                return detect_programming_language_from_code(code_segment)
        except IOError:
            return 'Unknown'
def detect_programming_language_from_code(code_segment):
    code_segment = code_segment.strip()
    patterns = {
        'Python': r'^import|from|def|\bprint\b',
        'Java': r'^import|public\s+class|void\s+main',
        'C++': r'^#include|using\s+namespace|int\s+main',
        'C': r'^#include|int\s+main',
        'HTML': r'^<html|<head|<body',
        'CSS': r'^\w+\s*{|\.\w+\s*{|\#\w+\s*{',
        'JavaScript': r'function\s+\w+|\$\(|console\.log',
        'PHP': r'<?php|echo|function\s+\w+',
        'Ruby': r'^require|def\s+\w+|puts',
        'Perl': r'^#!/usr/bin/perl|print|sub\s+\w+',
        'Swift': r'^import|class\s+\w+|func\s+\w+',
        'Go': r'^package\s+main|import\s+\(|func\s+\w+',
        'Rust': r'^fn\s+\w+|println!',
        'TypeScript': r'class\s+\w+|function\s+\w+|\$\(|console\.log',
        'Shell': r'^#!/bin/bash|echo|for\s+\w+\s+in',
        'SQL': r'^SELECT|INSERT|UPDATE|DELETE',
        'Prolog': r'^:-|,\s*\b[A-Z]\w*\b',
    }
    for language, pattern in patterns.items():
        if re.search(pattern, code_segment, re.MULTILINE):
            return language
    return 'Unknown'
if len(sys.argv) > 1:
    file_name = "./sample/"+sys.argv[1]
    language = detect_programming_language(file_name)
    print(f"The programming language is: {language}")
else:
    print("Please provide the file name as a command-line argument.")