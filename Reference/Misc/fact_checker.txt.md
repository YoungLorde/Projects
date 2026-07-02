#!/usr/bin/env python3  
"""  
Fact and Cross-Reference Checker  
Checks story codex, chapters for errors, inconsistencies, and cross-reference issues.  
"""

import re  
from pathlib import Path  
from typing import Dict, List, Set, Tuple  
from collections import defaultdict

class FactChecker:  
def __init__(self, chapters_dir: str, codex_dir: str = None):  
self.chapters_dir = Path(chapters_dir)  
self.codex_dir = Path(codex_dir) if codex_dir else None  
self.facts = defaultdict(list)  
self.issues = []

def load_codex(self) -> Dict:  
"""Load story codex if available."""  
codex = {}  
if self.codex_dir and self.codex_dir.exists():  
codex_files = self.codex_dir.glob('*.md')  
for codex_file in codex_files:  
with open(codex_file, 'r', encoding='utf-8') as f:  
codex[codex_file.stem] = f.read()  
return codex

def extract_facts(self, content: str, chapter_num: int) -> Dict[str, List]:  
"""Extract facts from content."""  
facts = {  
'dates': [],  
'names': [],  
'locations': [],  
'technologies': [],  
'numbers': []  
}

# Dates  
date_patterns = [  
r'(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}',  
r'\d{4}',  
r'(?:Spring|Summer|Fall|Winter) \d{4}'  
]

for pattern in date_patterns:  
matches = re.findall(pattern, content)  
facts['dates'].extend(matches)

# Names (capitalized words that appear to be names)  
name_pattern = r'\b[A-Z][a-z]+(?: [A-Z][a-z]+)*\b'  
names = re.findall(name_pattern, content)  
# Filter out common words  
common_words = {'The', 'A', 'An', 'In', 'On', 'At', 'To', 'For', 'With', 'By', 'From', 'And', 'But', 'Or', 'So'}  
facts['names'] = [name for name in names if name not in common_words and len(name) > 2]

# Numbers  
number_pattern = r'\b\d+(?:,\d+)*(?:\.\d+)?\b'  
numbers = re.findall(number_pattern, content)  
facts['numbers'] = numbers

return facts

def check_chapter(self, chapter_file: Path) -> Dict:  
"""Check a single chapter for issues."""  
with open(chapter_file, 'r', encoding='utf-8') as f:  
content = f.read()

chapter_num = int(chapter_file.stem.replace('chapter', ''))  
facts = self.extract_facts(content, chapter_num)

# Store facts  
for fact_type, fact_list in facts.items():  
for fact in fact_list:  
self.facts[fact_type].append({  
'value': fact,  
'chapter': chapter_num,  
'context': self._get_context(content, fact)  
})

# Check for issues  
chapter_issues = self._check_internal_consistency(content, chapter_num)  
self.issues.extend(chapter_issues)

return {  
'chapter_number': chapter_num,  
'facts': facts,  
'issues': chapter_issues  
}

def _get_context(self, content: str, fact: str) -> str:  
"""Get context around a fact."""  
index = content.find(fact)  
if index == -1:  
return ""  
start = max(0, index - 30)  
end = min(len(content), index + len(fact) + 30)  
return content[start:end].strip()

def _check_internal_consistency(self, content: str, chapter_num: int) -> List[Dict]:  
"""Check for internal consistency issues within a chapter."""  
issues = []

# Check for date contradictions  
dates = re.findall(r'(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}', content)  
if len(set(dates)) > 1:  
issues.append({  
'type': 'date_contradiction',  
'chapter': chapter_num,  
'description': f"Multiple different dates found: {', '.join(set(dates))}"  
})

# Check for number contradictions (same metric with different values)  
# This is a simplified check  
sp_matches = re.findall(r'SP Balance: ([\d,]+\.?\d*)', content)  
if len(set(sp_matches)) > 1:  
issues.append({  
'type': 'sp_contradiction',  
'chapter': chapter_num,  
'description': f"Multiple SP balance values: {', '.join(set(sp_matches))}"  
})

return issues

def check_cross_chapter_consistency(self) -> List[Dict]:  
"""Check for cross-chapter consistency issues."""  
issues = []

# Check for character name changes  
name_variations = defaultdict(set)  
for fact in self.facts['names']:  
name_variations[fact['value'].lower()].add(fact['value'])

for name_lower, variations in name_variations.items():  
if len(variations) > 1:  
issues.append({  
'type': 'name_variation',  
'description': f"Name variation detected: {', '.join(variations)}"  
})

return issues

def check_all_chapters(self) -> Dict:  
"""Check all chapters."""  
chapter_files = sorted(self.chapters_dir.glob('chapter*.md'))

for chapter_file in chapter_files:  
self.check_chapter(chapter_file)

cross_chapter_issues = self.check_cross_chapter_consistency()  
self.issues.extend(cross_chapter_issues)

return {  
'facts': dict(self.facts),  
'issues': self.issues  
}

def generate_report(self) -> str:  
"""Generate a comprehensive fact-checking report."""  
self.check_all_chapters()

report = "=" * 80 + "\n"  
report += "FACT AND CROSS-REFERENCE CHECKER REPORT\n"  
report += "=" * 80 + "\n\n"

report += "FACTS EXTRACTED:\n"  
report += "-" * 80 + "\n"  
for fact_type, facts in self.facts.items():  
report += f"{fact_type.title()}: {len(facts)} facts\n"

report += "\nISSUES FOUND:\n"  
report += "-" * 80 + "\n"  
if self.issues:  
for issue in self.issues:  
report += f"⚠ {issue['type'].upper()}\n"  
if 'chapter' in issue:  
report += f" Chapter: {issue['chapter']}\n"  
report += f" Description: {issue['description']}\n\n"  
else:  
report += "✓ No issues detected.\n"

return report

if __name__ == "__main__":  
checker = FactChecker(r"c:\dev\myriad\apps\web\src\ui\data\chapters")  
print(checker.generate_report())