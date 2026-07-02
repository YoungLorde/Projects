---
**Date:** 2026-01-02 → 2026-01-05
**Arc:** Arc 1 — Software Wealth Building (Ch 1–50)
**Location:** Louisville, KY — Preston Street apartment; Louisville Free Public Library; Keen American Built break room and office
**Cultivation:** Mohamed — Rank 0, Level 0 (subtle physical changes persist); Danielle — not yet a cultivator
**Lifespan:** Mohamed — ~80 years; Danielle — ~80 years
**SP Balance:** 0.8 SSP → 28.400000245 SSP
**Fiat Balance:** $137.30 → $567.62 (paycheck +$1,200.04; rent -$700; food/groceries -$69.72)
**Passive SP/hr:** 0.000000245 (2 users)
**Total Users:** 0 → 2
**Key Characters:** Mohamed Vance, Danielle Jones (introduced), Patricia (cameo), DeWitt (cameo)
**Technologies Introduced:** VanceFlow v0.1 (TECH-004)
**Items Introduced:** None
**Skills Used/Unlocked:** VanceFlow Implementation (SKILL-003)
**Locations Visited:** Preston Street apartment, Louisville Free Public Library, Keen American Built break room and office
**Factions Involved:** Keen American Built, VanceFlow (informal)
**Karma Events Seeded:** KSEED-004 (Danielle's technical skill will become empire-critical), KSEED-005 (Keen's paperwork problem is a microcosm of every small manufacturer's pain), KSEED-013 (Danielle's suspicion about Mohamed's speed will drive future tension)
**StoryDB IDs Created/Updated:** TECH-004, TECH-005, TECH-006, SKILL-003, CHAR-002, CAMEO-003, REL-001 (updated), REL-011, REL-012, KNOW-009, KNOW-010, KSEED-004, KSEED-005, KSEED-013, SP-004, SP-005, SP-006, SP-007, FIAT-003, FIAT-004, FIAT-005, FIAT-006, FIAT-007, FIAT-008, USER-003, USER-004
**Word Count Target:** 6,000
---

Mohamed Vance did not sleep on January 1st. He napped in forty-minute intervals, woke with the blueprint burning behind his eyes, and typed until his laptop fan sounded like a dying animal.

By the morning of January 2nd, VanceFlow had a name, a folder, a database schema, and a brutal honesty problem. It could identify the word *INVOICE* on a scanned page nine times out of ten. The tenth time it mistook it for a coffee stain and crashed.

He fixed the crash. He drank three cups of coffee. He ate a packet of saltine crackers he found in the back of a cabinet. Then he fixed it again.

The blueprint in his head was not code. It was architecture: a pipeline that took a document in one end and returned structured data out the other. The individual pieces were simple. The hard part was making them talk to each other without lying. OCR was a liar. It would read a *5* as an *S*, a *1* as an *l*, a *0* as an *O*. Mohamed had to build a confidence scorer that flagged uncertain characters and a human-review queue that made the lies obvious.

He built it in Python. He had learned Python in college, before the expulsion, and had kept it alive by writing scripts for the shop floor — small utilities that calculated feed rates, tool paths, nothing impressive. Now he had a blueprint that made him write better than he knew how.

The blueprint was not a cheat. It was a ladder. Every rung required him to climb.

By noon on January 2nd, VanceFlow could ingest a two-page PDF invoice and return a JSON object with vendor, date, line items, total, and a confidence score. The confidence score was frequently wrong. Mohamed marked those cases in a notebook and kept going.

He slept four hours on the couch. He woke at six in the evening, made ramen, and worked until three in the morning.

On January 2nd, his bi-weekly paycheck from Keen cleared — $1,200.04, after taxes and the union dues he had forgotten he paid. He spent $7.50 that same day on coffee and a sandwich from the corner store because he had not gone grocery shopping in three weeks and the cabinet held only saltines and ramen. He also paid his January rent — $700 to the landlord on Preston Street, transferred from his phone while he was still in bed, the way he paid it every month: early, automatically, before the money could tempt him into spending it on something else. The balance after rent and food was $629.84, which was still more than he usually had at the start of a month. He worked through the night, and when he slept, he slept on the couch.

On January 3rd, he bought coffee at the corner store with three crumpled dollars and realized he had not checked his bank account since Friday. The balance read six hundred twenty-one dollars and forty-four cents. Rent had eaten the usual chunk — $700 to the landlord, gone before it could tempt him — but the paycheck had softened the blow. He also stopped at the supermarket on Preston Street and spent $47.32 on rice, beans, coffee, eggs, bread, and apples — the first real groceries he had bought in six months. The cabinet would not look like a famine zone for a while. The balance after groceries was $574.12.

He looked at the thin blue line at the bottom of his vision. He could expand it into the full catalog whenever he wanted. He did not. The catalog was a distraction now. He had spent 0.2 SSP on a tutorial and a blueprint. He had 0.8 SSP left. He would not spend another point until he knew what the next purchase should be.

He finished the prototype at 2:17 AM on January 4th.

It was ugly. The dashboard looked like a spreadsheet had a child with a command prompt. The upload button was a gray rectangle with the word *Upload*. The results table had no colors. The error messages were written in the clipped, defensive tone of a man who had spent too much time around machines.

But it worked.

Mohamed uploaded a test invoice he had pulled from the Keen American Built trash — a supplier invoice for carbide inserts, already paid, no longer sensitive. VanceFlow read it. It flagged three uncertain characters. It extracted the vendor, the part numbers, the quantities, the unit prices, and the total. It was correct.

Mohamed sat in his chair and did not move for two minutes.

Then he did the math. If the office manager at Keen spent three hours a day typing invoices, and VanceFlow cut that to thirty minutes, the tool was worth money. Real money. Subscription money. Small businesses paid for time the way drowning men paid for air.

He ran a second invoice. Then a third. He uploaded a packing slip. He uploaded a purchase order. He uploaded a handwritten receipt from the corner deli just to see if it would break. It broke. He fixed the break. He uploaded it again. It returned a vendor name, a date, and a total with seventeen uncertain flags. The uncertain flags were correct.

The biggest problem was the table extractor. Invoices were not tables in the way a spreadsheet understood tables. They were visual arrangements of boxes and lines, and the lines did not always connect. A line item might be split across two rows because the description was long. A quantity might be in the same column as a unit price because the invoice designer had been lazy. A total might be at the bottom right, or the bottom left, or under a bold label that said *PLEASE PAY THIS AMOUNT*.

Mohamed spent three hours on the table extractor. He wrote a heuristic that looked for the word *TOTAL*. He wrote another that looked for columns with numbers. He wrote a third that tried to match line items by vertical alignment. None of them worked on every invoice. All of them worked on some. The final extractor was a mess of if-then rules that would have embarrassed him in college, but it worked on the invoices he had.

That was the lesson of the first build: perfect was the enemy of shipped. He could spend a year making the extractor beautiful and general, or he could spend a week making it work on the documents his first customers actually had. He chose the week. The System had not taught him business, but it had taught him architecture, and architecture was about choosing the right trade-offs.

He stood up and walked around the apartment. It was four in the morning. The radiator clanked. The upstairs neighbor was either moving furniture or fighting with someone. Mohamed did not care. He had made a thing, and the thing did what it was supposed to do.

That was a kind of wealth he had never owned before.

He sat back down and wrote a list of what was missing: user authentication, a database, an export function, a real dashboard, error logging, a terms of service, a payment flow. It was a long list. But the core was real. The core was a machine that turned paper into data.

He needed a test. A real test. A human test.

He needed to go back to work.

---

On January 4th, Mohamed went to the Louisville Free Public Library.

He had not been there in years. The building was a limestone block on York Street, warm inside despite the cold, smelling of old paper and the floor polish the janitors used at night. He walked past the fiction shelves, past the children's section, past the magazine rack with its tattered copies of *Car and Driver*, and found a computer carrel in the corner of the technology section.

He sat down and opened a browser. He needed a domain name. He needed hosting. He needed a GitHub account. He needed all the public artifacts that would make his cover story believable.

He registered vanceflow.io. The domain cost twelve dollars. He paid with a prepaid debit card he had bought at the gas station, the kind that did not require a name. He did not want VanceFlow connected to Mohamed Vance until he had to make it connected. He chose Namecheap because it was cheap and did not ask many questions.

He signed up for a free tier on AWS. He created a GitHub account under the name "vanceflow-dev" and pushed a single README file that described VanceFlow as an "experimental document automation project." He created a private repository for the real code and pushed the prototype. He made the first commit at 10:47 AM with a message that read: *Initial pipeline for OCR-based invoice extraction.*

He sat back and looked at the screen. The public artifacts were thin. They would not survive a serious investigation. But they would survive a casual question. If someone asked how he learned to code, he could point to the library. If someone asked where the code was, he could point to GitHub. If someone asked how long he had been working on it, he could point to the commit history.

The cover story was not perfect. It was a fence, and fences could be climbed. But it was better than nothing.

He spent two hours reading documentation. He read about Tesseract, about OpenCV, about Flask, about PostgreSQL. He already knew most of what he read, but he needed the browser history to show that he had looked. He bookmarked pages. He opened tabs. He made notes in a cheap notebook with a Louisville Free Public Library stamp on the cover.

A librarian walked past, pushing a cart of books. She was older, with silver hair tied in a bun, and she moved with the deliberate patience of someone who had spent decades among shelves. She glanced at his screen, saw the code and the documentation, and smiled.

"Learning to code?" she asked.

"Yes, ma'am."

"Good for you. The library has a free Udemy login if you want structured courses."

"Thank you. I'll look into it."

She moved on. Mohamed watched her go. It was a small exchange, but it was a witness. If anyone ever asked where he learned to code, he could mention the Louisville Free Public Library, the Udemy login, the documentation, the librarians. The cover story was built from real places and real people, and that was what made it survive.

He also checked out a book on Python web development, one on machine learning basics, and one on small business accounting. He did not need them, but they would sit on the shelf in his apartment, visible, lending credibility. He was building a room of evidence.

When he left, he felt the way he imagined a spy must feel. The library was a stage. He had performed his role, and the audience was anyone who would ask questions later.

The walk back to his apartment was shorter than the walk from the shop. He bought a sandwich and a coffee for $8.40 at a deli on the way. The coffee was burnt. The sandwich was dry. He ate it on the steps of his apartment because he was too tired to go inside.

He thought about the day. He had spent twelve dollars on a domain. He had spent eight dollars and forty cents on lunch. He had spent nothing on the knowledge that would build his empire. The System had given him the blueprint for 0.1 SSP, and 0.1 SSP was worth ten thousand dollars in the secret exchange rate. He had paid ten thousand dollars' worth of purchasing power for a design that would have taken a team of engineers months to produce. It was the best deal he would ever make, and he had made it without understanding how good it was.

He also thought about the risk. The System was a secret he had to keep forever. The cover story was a lie he had to maintain forever. Every person he brought into VanceFlow was a witness, a potential questioner, a person who might wonder why his code was better than it should be. The more users he had, the more witnesses he had. The more witnesses he had, the more careful he had to be, and the more valuable the secret became.

But the alternative was to stop. The alternative was to put the interface away and go back to the factory floor and live inside tolerance for the rest of his life. He had tried that. He knew how it ended. He would not choose it again, not when the ladder was finally in his hands.

He had $567.62 left. Rent and groceries had eaten most of the paycheck, the way they always did, but the cabinet was stocked for the first time in months and the landlord would not come knocking. It was not enough to quit Keen. It was not enough to rent an office. It was not enough to do anything except survive while he built.

He would have to make VanceFlow generate real money before he could buy anything else from the System. The System had given him the map, but the map was not the journey. He had to walk the journey in public, wearing his cover story like a coat.

---

The Keen American Built break room smelled of burnt popcorn and industrial hand soap. Mohamed sat at a corner table with his laptop open, the screen angled away from the door. He had worked the Sunday afternoon shift, a quiet four-hour block that DeWitt had scheduled him for because no one else wanted it. On the way in he had spent $6.50 on a sandwich and a coffee from the gas station, another small subtraction from the paycheck that had made him feel rich two days ago.

The shift had been uneventful. He had run three parts, checked two more, and spent the slow hours thinking about the table extractor. The problem with building in his head was that he could not stop. Even when his hands were on the Haas mill, his mind was on the code. He had nearly made a setup error because he had been thinking about column alignment. He caught himself in time, but the mistake shook him. He could not let the System distract him from the machines. The machines could hurt him. The System could not hurt him, but it could make him careless.

The office manager, a woman named Patricia, walked in at 3:30 with a stack of paper invoices and a mug that read *World's Okayest Mom*. She sat at the small desk in the corner — the desk that was technically in the break room because the company had run out of office space five years ago — and began typing.

Mohamed watched her from behind his laptop. He had watched her do this dozens of times. He had never thought about it. Now he saw every wasted motion: the flip back to the previous page, the squint at a smudged number, the sigh when the spreadsheet formula broke, the phone call to a supplier because the quantities did not match.

Patricia worked for three hours every afternoon. She was paid $18.50 an hour. That was $55.50 a day. Over a year, assuming 250 workdays, that was $13,875 of salary spent on typing numbers from paper into a screen. And that did not count the mistakes. Or the late payments. Or the supplier arguments. Or the overtime.

Mohamed's hands were steady on the keyboard. The small tremor he usually had after a shift was still gone. His vision was sharper. He could read the tiny numbers on Patricia's invoices from fifteen feet away. He told himself it was the coffee. He had told himself that for three days.

He stood up, walked to the coffee maker, and poured a cup he did not want. Then he turned to Patricia.

"Patricia," he said.

She looked up, blinking. "Mohamed. You scared me. I didn't know you were in here."

"Sorry. I was in the corner."

"You always are." She smiled. It was a tired smile. "What's up?"

He had rehearsed this. He had rehearsed it in the mirror at 4 AM, in the shower, while walking to work, while lying awake in the dark. The cover story was the whole point. He was a self-taught developer. He had read obsessively. He had built a thing in his spare time. He was not a man with a multiversal shop in his head.

The trick to a lie was not making it elaborate. The trick was making it boring. People did not question boring stories. They questioned extraordinary ones. A self-taught machinist who built invoice software in his spare time was strange, but it was not impossible. Stranger things happened every day. The world was full of people who taught themselves skills online and made things that surprised their coworkers. Mohamed only had to be one of those people, and he had to be boring enough that no one asked the interesting questions. Boring was safe. Boring was invisible. Boring was the best camouflage.

"I've been working on a small software project," he said. "It's a tool that reads invoices and turns them into spreadsheet data. I was wondering if you'd be willing to try it. On one invoice. Just to see if it works."

Patricia's expression was polite, the expression of a woman who had been asked to try many things by many people and had learned to say no kindly.

"Mohamed, that's sweet, but I've got forty of these to do before five."

"I know. That's why I'm asking. This could do them in five minutes."

She laughed. It was not mean. "Honey, I've been hearing that since 1998. Every year some salesman tells me his software is going to save my job."

"I'm not a salesman."

"No. You're a machinist who does magic tricks with metal."

"No magic," he said. "Just code. And it's free to try."

She sighed, a sound that came from a place deeper than irritation. It was the sound of someone who had been disappointed enough times to expect disappointment. "I don't have time to be your guinea pig."

"One invoice. If it doesn't work, you never see me again."

She studied him. Mohamed was not a talker. The machinists joked that he spoke in machine language. For him to ask her anything was unusual enough to make her curious.

"One invoice," she said. "And if you break my spreadsheet, I tell DeWitt you owe me a chocolate cake."

"Deal."

He sat down at the desk next to her and opened VanceFlow. Patricia watched the gray screen appear. She did not look impressed.

"Upload the worst one," Mohamed said.

She pulled a crumpled invoice from the bottom of the stack. It was from a supplier in Cincinnati, water-damaged on one corner, the numbers smeared by what looked like coffee. "This one took me twenty minutes last week. I had to call them twice."

Mohamed scanned it with his phone, uploaded the PDF, and clicked the gray button.

The screen went blank for three seconds. Then a table appeared.

Vendor: Tri-State Industrial Supply.
Date: 2025-12-18.
Line items: six.
Total: $4,847.33.
Uncertain fields: two, highlighted in yellow.

Patricia leaned forward. She did not say anything for ten seconds. Then she pointed at the yellow highlight.

"That's the quantity on item four. I couldn't read it either."

"Yes," Mohamed said. "It flagged it for you."

She clicked the uncertain field. The original image appeared beside the extracted text, zoomed in. The number was either a *7* or a *1*. Patricia looked at the context, clicked *7*, and the table updated.

"Oh," she said. "That's... actually helpful."

"It can export to Excel. CSV. JSON. Whatever your system wants."

"Who made this?"

"I did."

She stared at him. "You?"

"I read a lot."

Patricia laughed again, but this time it was different. It was the laugh of someone who had just seen a magic trick and was trying to decide if it was real.

"Mohamed, this is good. This is actually good."

He felt something in his chest he did not have a name for. It was not happiness. It was closer to relief. He had spent his life making parts that fit inside machines he would never own. Now he had made something that fit inside a human process, and a human had seen it work.

"It's not ready yet," he said. "I need to test it more."

"You should show DeWitt."

"Not yet."

"Why not?"

Because the next question would be *how did you learn to do this?* and Mohamed did not have an answer that would survive follow-up questions. Because the System was a secret. Because if anyone looked too closely, they would find the shop in his head, and the shop would not explain itself.

"It's not polished enough," he said. "I don't want to embarrass myself."

Patricia nodded, the way women nodded when they knew a man was lying but decided not to push. "Fair enough. But you let me know when it is. I'll buy the first license myself."

She was joking. Mohamed wrote it down in his mental ledger as a real promise.

---

The break room door opened at 4:45, and a woman walked in who made Mohamed forget what he was about to say.

She was small. Five-foot-one, maybe. Petite, blonde, with green eyes that looked like they had already cataloged every flaw in the room. She wore a navy jacket over a gray hoodie, and she carried a laptop bag that had been repaired with duct tape on one corner. She went straight to the coffee maker, poured the last of the pot, and turned around.

"Patricia," she said, "the router in the data entry room died again. I'm using the break room until IT fixes it. Which will be never."

"Danielle, you know the rules. The break room is sacred."

"The break room is where the coffee is. That's the only rule I care about."

She sat at the table across from Mohamed. She did not look at him. She opened her laptop, plugged in a power cable, and began typing with a speed that suggested she had learned to type before she learned to walk.

Mohamed watched her for three seconds. Then he made himself look back at his screen.

He knew who she was. He had seen her in the hallways — a data entry temp, moved from department to department, never permanent. The other machinists had a nickname for her that Mohamed did not use. He had noticed her because she was the only person at Keen who looked at machines the way he did: with the expression of someone who understood that the machine was a lie and the truth was in the code.

She was typing in a terminal. Not a browser. Not a spreadsheet. A terminal. Black background, green text. She hit an error, muttered something under her breath that sounded like "you absolute garbage compiler," and kept going.

Mohamed recognized the profanity. He had used it himself.

He should not talk to her. He had a secret. He had a prototype. He had a plan that did not include being noticed by a sharp-eyed woman who worked with computers.

But she was sitting three feet away, and she was typing in a terminal, and she had duct tape on her bag, and she had just insulted a compiler in exactly the way he would have. The coincidence felt like a trap. The universe was baiting him.

He kept his eyes on his screen. He tried to think about invoices. He tried to think about OCR confidence scoring. He tried to think about anything except the fact that the woman across from him was clearly brilliant and clearly suspicious and clearly the kind of person who could unravel a cover story in three questions.

She pulled a protein bar from her jacket pocket and unwrapped it with one hand while typing with the other. Mohamed had never seen anyone do that. He watched her do it for ten seconds before he realized he was staring again.

She looked up at him. Her eyes were green and direct.

"You're staring," she said.

"You're swearing at your compiler."

"And you're staring."

"Fair."

She looked back at her screen. "I don't recognize you from the office side."

"I'm not. I'm on the floor."

"CNC?"

"Yes."

"Huh." She typed for another ten seconds. "You don't look like the usual floor guys."

"How do I look?"

"Tired. And like you're pretending to be invisible."

Mohamed did not know what to say to that. He had spent years perfecting invisibility. He had not expected someone to name it in a break room.

Patricia, who had been watching the exchange with the amusement of a woman who had seen many things, spoke up. "Danielle, Mohamed just showed me the most interesting thing."

"Interesting how?"

"Software. It reads invoices."

Danielle's fingers stopped typing. She looked at Mohamed's laptop screen, then at Mohamed, then at the screen again. "Let me see."

Mohamed turned the laptop toward her. He did not want to. He wanted to hide VanceFlow under his jacket and leave. But Patricia was already talking, and Danielle was already looking, and he had learned enough about momentum to know when a thing was in motion.

He watched Danielle's face as she examined the interface. She did not smile. She did not nod. She looked the way his father had looked at an engine that someone had claimed was rebuilt: skeptical, patient, waiting for the flaw to reveal itself. She clicked through every screen. She read the error messages. She checked the export format. She was not testing whether it worked. She was testing whether it was real.

Danielle clicked through the interface. She uploaded the invoice Patricia had used. She watched the results table appear. She clicked the yellow uncertain field. She examined the JSON export.

"Where did you get the OCR engine?" she asked.

"Tesseract. Open source."

"And the layout parser?"

"Custom."

"The confidence scoring?"

"Custom."

"The table extraction?"

"Custom."

She looked at him the way a mechanic looked at an engine that had been rebuilt with parts that should not fit together. "You built this alone?"

"Yes."

"When?"

"Over the weekend."

She laughed. It was short, sharp, and not friendly. "Bullshit."

"It's true."

"Nobody builds this in a weekend."

"I did."

Danielle leaned back in her chair. "Okay. Prove it."

"How?"

"Show me the repo."

Mohamed hesitated. The repo was on his laptop, private, pushed to a GitHub account under a name that had no connection to him. He had done that on the second night, while the System interface glowed at the bottom of his vision, reminding him that he was now a man who had to hide everything.

"Not here," he said.

"Why?"

"Because it's not ready."

"It's not ready but you built it in a weekend. Pick one."

"I built a rough version in a weekend. It's not ready for inspection."

Danielle studied him. Her eyes were not hostile. They were curious in a way that made Mohamed think of predators. She was smart. She was dangerous. She was exactly the kind of person he should avoid.

"Fine," she said. "But when you show someone, you show me."

"Why?"

"Because I can tell if you're full of shit. And because I know what this could actually be."

She closed her laptop, stood up, and walked out of the break room with her coffee. The duct tape on her bag caught the light for a moment, then she was gone.

Patricia looked at Mohamed. "Well. That went well."

"Did it?"

"Danielle doesn't talk to anyone. She just talked to you for five minutes. That's a record."

Mohamed looked at the door. He thought about the way she had looked at VanceFlow. Not as a curiosity. As a tool. As a weapon.

He thought: *I need to be careful around her.*

He also thought: *I need her.*

---

That night, Mohamed worked until 4 AM. He did not sleep. He added user registration to VanceFlow. He added a simple database. He added a dashboard that showed how many documents had been processed. He added an export function that actually worked.

He also added a terms of service page he copied from a template, changed the company name to "VanceFlow," and created a registration flow.

At 5:47 AM on January 5th, he sent an email to Patricia from a Gmail account he had created: *vanceflow.beta@gmail.com*. The email contained a link and a login. He asked her to try it on one invoice from home.

At 6:12 AM, she replied: *It works. I uploaded three. How much?*

Mohamed read the email three times. Then he forwarded it to Danielle from the same account, because he had found her work email in the company directory. He wrote: *You said you wanted to see it. Try it. One invoice. Tell me what's wrong.*

Danielle replied at 6:41 AM: *The OCR chokes on handwritten notes. The confidence scorer is too generous. The JSON schema is ugly. The dashboard is an eyesore. But it works. I'm user #2.*

Mohamed opened the VanceFlow database. Two users. Patricia and Danielle.

He expanded the System interface. He had not looked at it in days. The balance still read 0.8 SSP. Two users, the terms of operation said, should generate a first-use bonus. He did not know how much. He did not know when it would arrive. He only knew that the System paid immediately, per user, and that the amount fluctuated.

He watched the balance for ten seconds. Then it changed.

**BALANCE: 0.813500 SSP**

A notification appeared in the corner of his vision:

**NEW USER: Patricia Hart. FIRST-USE BONUS: +13.500000 SSP.**

Mohamed stared at the number. It was more than he had spent on the Interface Guide and the blueprint combined. It was more than he had made in his first three days at Keen. It was just for one person using a thing he had built.

Before he could process it, another notification appeared:

**NEW USER: Danielle Jones. FIRST-USE BONUS: +14.100000 SSP.**

The balance updated again:

**BALANCE: 28.400000 SSP**

A third line appeared, smaller, almost an afterthought:

**PASSIVE SP: +0.000000245 SSP (2 users, 0.0000001225 SSP/hr)**

The final balance read: 28.400000245 SSP.

Mohamed sat very still.

He had not expected the numbers to be so large. He had not expected the act of giving someone a tool to feel so much like printing money. He understood, in a way that made his stomach tight and his hands still, that the System did not care about fairness. It cared about use. Every person who used VanceFlow would drop 10–17 SP into his account, immediately, with no delay and no accumulation threshold, and the only thing he had to do was keep making things worth using.

The fluctuation was not random in a threatening way. It was random in a natural way, like the variation in metal grain or the way a machine's cut drifted by thousandths of an inch. Some users would be worth more. Some would be worth less. The average would be around 13.5, but the exact value was a property of the user, not a rule.

Patricia had been 13.5. Danielle had been 14.1. He did not know why. He did not need to know why. He needed to know that the next user would add another 10–17, and the next, and the next, and the next, until the numbers became large enough to buy the next blueprint.

He also understood the trap. If the money came too easily, he would stop thinking about the people using the tool. If he stopped thinking about the people, the tool would stop being useful. If the tool stopped being useful, the people would stop using it, and the SP would stop flowing. The System was not a bank account. It was a feedback loop. The value it paid was proportional to the value he created, and the only way to create more value was to understand the people who needed it.

He had spent his life as one of those people — the invisible, the overworked, the broke. He understood the small manufacturer, the overtaxed office manager, the temp who typed invoices until her wrists hurt. That understanding was the real edge. The System gave him blueprints. His life gave him empathy.

He closed the interface and looked at the apartment. Dawn was breaking over Louisville. The radiator clanked. The upstairs neighbor was silent. He had not slept in thirty hours, but he felt more awake than he had in years.

Two users. Twenty-eight point four SSP. A tool that worked. A woman who could see through him. A plan that was beginning to move.

He opened the notebook from the drawer and added a new line:

*7. Danielle Jones is dangerous. Keep her close. She can build what I cannot yet do alone. The cost is scrutiny. The cost is worth it.*

*8. First-use bonuses vary per user. Track exact amounts. Never assume an average.*

*9. Two users in three days. If the rate continues, I will have enough to buy the next blueprint within weeks. The next purchase should be something that makes VanceFlow better: security, marketing, or a deeper technical foundation. The choice depends on what users ask for.*

He closed the notebook and hid it under the T-shirts.

Then he lay down on the bed and slept for six hours, the first real sleep he had allowed himself in five days. When he woke, he would go to work, and the world would look the same, but he would be different. He had a product. He had users. He had a path.

The factory floor would still smell of cutting fluid. DeWitt would still have the same mustache. Patricia would still type invoices. Danielle would still be suspicious. But the secret would be larger now, and the secret would grow every time someone uploaded a document. That was the nature of the System. It did not make a man powerful. It made a man powerful in proportion to what he built, and Mohamed had finally begun to build.

He had 28.400000245 SSP, and he knew exactly what it could buy next. He also knew exactly how much it would cost.

He also knew, with the clarity of a man who had finally seen the first turn of a very long road, that his life would never be small again. He had a product. He had users. He had money that no bank could see and knowledge that no school could teach. The only thing standing between him and the next blueprint was the work he had already decided to do.

He closed the interface, set his alarm for four hours, and let himself fall into sleep. The last thing he saw before his eyes closed was the thin blue line at the bottom of his vision, patient and strange, a secret he would carry for the rest of his life.

**In-story date stamp: 2026-01-05, 11:41 AM, Louisville, KY.**
