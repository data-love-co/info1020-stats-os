# Get GitHub Copilot for free

*A step-by-step guide for DU students. Plan on about 20 minutes of clicking plus a wait of a few minutes to a few days for GitHub to verify that you are a student. You will never be asked to pay for anything in this course.*

## What you are getting and why

This course lets you pick one generative AI tool for the AI Blocks. GitHub Copilot is a good choice because verified students get it free, it answers questions in a chat window (like ChatGPT or Claude), and it also works inside a code editor if you ever write Python, R or SQL. There are two free versions, and you can have both: start with Copilot Free today, then switch to Copilot Student once GitHub confirms you are a DU student.

|                                   | **Copilot Free**                  | **Copilot Student**                        |
|-----------------------------------|-----------------------------------|--------------------------------------------|
| **Who**                           | Anyone with a GitHub account      | Students verified through GitHub Education |
| **Cost**                          | Free                              | Free, re-checked by GitHub each month      |
| **Chat questions**                | A monthly allowance of AI credits | A monthly allowance of AI credits (larger) |
| **Code suggestions in an editor** | Up to 2,000 per month             | Unlimited                                  |
| **Model choice**                  | Automatic only                    | Automatic only                             |
| **Time to get it**                | About 5 minutes                   | 20 minutes plus the verification wait      |

**One thing to know before you start:** GitHub Copilot is not the same product as the Microsoft Copilot button you may see in Windows, Edge or Office. This guide is only about GitHub Copilot, which lives at github.com and inside Visual Studio Code.

## Before you start, have these ready

- **A personal GitHub account.** If you do not have one, create it at github.com/signup. Use a personal email address you will still have after you graduate, and pick a username you would be comfortable showing an employer. One account per person; GitHub does not allow a second one.

- **Your DU email address.** GitHub uses your @du.edu address as the main proof that you are a student. You will add it to your GitHub account in Step B.

- **Proof of enrollment, just in case.** A photo of your DU student ID, or a screenshot of your Fall 2026 class schedule that shows your name and the term dates. GitHub sometimes asks for one of these even when your DU email checks out.

- **A place on campus and a phone.** The application asks your web browser for your location to confirm you are near campus. Laptops often get this wrong. Doing the application on your phone, on campus, with location services on and any VPN off, is the most reliable way through.

## Step A: turn on Copilot Free today (5 minutes)

Do this first so you have a working tool while the student application is being reviewed.

1.  Sign in to GitHub and go to [github.com/copilot](https://github.com/copilot).

2.  If you see a "Start using Copilot Free" or "Get started" button, click it. Accept the terms. If you land straight in a chat window, you already have it.

3.  Two settings will appear at some point in this process: "Allow suggestions matching public code" and whether GitHub may use your prompts to improve the product. Either answer is fine for this course; many students turn the second one off.

4.  Type a question in the chat box to confirm it works. Try: "In plain language, what does a p-value of .03 mean?"

## Step B: apply to GitHub Education (10 minutes)

1.  Add your DU email to your GitHub account: click your profile picture (top right), then **Settings**, then **Emails**. Add your @du.edu address, then click the verification link GitHub sends to that inbox. Keep your personal email as the primary one.

2.  Go to [github.com/settings/education/benefits](https://github.com/settings/education/benefits) and click **Start an application**. Choose **Student**.

3.  Type "University of Denver" as your school and pick your @du.edu address from the email list. Answer the short question about how you plan to use GitHub in a sentence or two (for example, "coursework for INFO 1020 Analytics II and personal projects").

4.  When the page asks to check your location, click **Allow**. This is the step that trips people up. If GitHub says it cannot confirm you are near campus, close the browser, open the same page on your phone with location services on, Wi-Fi off, cellular data on, and any VPN off, and try again from campus.

5.  If GitHub asks for proof, upload the photo or screenshot you prepared. It must be readable and it must show a current date or the Fall 2026 term. A blurry ID or a schedule with no dates is the most common reason for a denial.

6.  Click **Submit application**. Some applications are approved within minutes; others take a few days. You will get an email either way, and the Education benefits page shows your status.

**If you are denied:** read the reason in the email, fix that one thing (usually clearer proof or a verified DU email), and apply again from the same page. There is no limit on reapplying and no penalty for a denial.

## Step C: activate Copilot Student after approval (5 minutes)

Approval and activation are two separate steps. Being approved for GitHub Education does not switch Copilot on by itself.

1.  Go back to [github.com/settings/education/benefits](https://github.com/settings/education/benefits). Under "Free GitHub developer resources for students and teachers," click **Learn more** and follow the prompts to activate Copilot.

2.  If that page does not offer Copilot yet, try [github.com/settings/copilot](https://github.com/settings/copilot) and look for a button to get access to Copilot.

3.  Confirm the plan name on the Copilot settings page reads **Copilot Student**, not Copilot Free.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>If you only see paid options</strong></p>
<p>GitHub says the student benefit "can take several days to finish applying after verification." Do not buy anything. Wait a few days and check the two pages above again. If you still see only paid plans after a week, contact GitHub Support from support.github.com and mention that your Education application was approved on the date shown in your email.</p>
<p>GitHub re-checks student eligibility monthly and the Education benefits themselves last about two years. If Copilot Student disappears mid-term, go back to Step C and, if needed, reapply from Step B.</p></td>
</tr>
</tbody>
</table>

## Step D: where to use it

### On the web (all you need for the AI Blocks)

Go to [github.com/copilot](https://github.com/copilot) while signed in. This is a normal chat window. Paste the AI Block prompt from the module, add the numbers from your workbook, and ask for what you need: a plain-language interpretation, a check on your manager sentence, or an explanation of an Excel formula you do not understand.

### In Visual Studio Code (the Tier 2 setup)

This is what you need if you want the agent to read the workspace folder and run the AI Blocks for you instead of pasting prompts into a chat window. Nothing in the course requires it, and everything on the web still works without it.

1.  Download Visual Studio Code free from [code.visualstudio.com](https://code.visualstudio.com) and install it.

2.  Install the GitHub Copilot extension. Open the Extensions view in the left sidebar (the four-squares icon), search for "GitHub Copilot," and click **Install**. Recent versions of VS Code already include it, so if you can see a Copilot icon, skip this step.

3.  Sign in with the GitHub account that has your Education benefits on it. Click the Copilot icon, choose to sign in, and finish in the browser window that opens. Use the same account you verified in Step B, or Copilot will run on the wrong plan.

4.  Open the Chat panel: **Ctrl+Alt+I** on Windows, **Control+Command+I** on a Mac. The speech-bubble icon near the top right does the same thing.

5.  Find the mode picker at the bottom of the chat panel and switch it from **Ask** to **Agent** when you are ready to run a block. That picker is how you follow "Ask for questions, Agent for blocks" below.

6.  Install two more things once, and you are done for the term. **Git** from [git-scm.com](https://git-scm.com), which is what the clone step uses to copy the workspace onto your machine, and **Python 3** from [python.org](https://www.python.org/downloads/), which the skills use to compute for real. On Windows, tick **Add Python to PATH** in the Python installer; if you miss it, the skills will not be able to find Python.

Code suggestions still appear in grey as you type, in either mode. Press Tab to accept one. They do not spend credits.

## Make your monthly allowance last

Both free plans meter chat with "AI credits" that reset on the first of each month. GitHub does not publish an exact number for the student plan; students report a small allowance, enough for a few dozen ordinary chat questions and far fewer if you use agent mode. Code suggestions do not use credits. Four habits keep you well inside the limit:

- Ask one complete question per message. Give the numbers, the context and what you want back in a single message instead of a back-and-forth.

- Start a new chat for each new topic. Long conversations re-read everything above, which spends credits faster.

- Ask for questions, Agent for blocks. Agent mode, where Copilot reads the workspace and runs things on its own, costs many times more per request than Ask does. That cost is the reason to aim it at the work that needs it: running an AI Block on Tier 2, which from Module 2 onward means code that has to actually run. Everything smaller, a concept question, a formula you want explained, a sentence you want checked, belongs in Ask.

- If chat pauses for the month, that is the limit, not a bug. Code suggestions keep working, the credits return on the first, and you can use the free tier of another tool (Claude, ChatGPT, Gemini) for that AI Block. You do not need to buy credits.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>The course rules for any AI tool, Copilot included</strong></p>
<p><strong>Verify.</strong> Every number and every claim gets checked against your own workbook before it goes in your answer.</p>
<p><strong>Cite.</strong> Say which tool you used and paste the prompt where the AI Block asks for it.</p>
<p><strong>Add value.</strong> The AI drafts, you decide. Your manager sentence has to be yours.</p>
<p><strong>Never on quizzes or exams.</strong> AI tools are for labs, AI Blocks and the project only.</p></td>
</tr>
</tbody>
</table>

## Troubleshooting

| **What you see**                                        | **What to do**                                                                                                                                                          |
|---------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "We could not verify your location"                     | Do the application on your phone from campus: location services on, Wi-Fi off, cellular on, VPN off, and allow the location request in the browser.                     |
| "Your academic email domain is not recognized"          | Make sure the @du.edu address is added AND verified under Settings, Emails, then upload your student ID or schedule as proof.                                           |
| Denied for unclear documents                            | Retake the photo in good light so the name, the school and a current date are all readable. A Fall 2026 schedule screenshot from MyDU works well.                       |
| "This email is already associated with another account" | You have an older GitHub account using your DU email. Sign in to that one instead, or remove the DU email from it first. GitHub allows one personal account per person. |
| Approved, but Copilot still says Free                   | Approval and activation are separate. Do Step C. If only paid plans appear, wait several days and try again; do not pay.                                                |
| No model picker in chat                                 | Normal. Both free plans use automatic model selection only.                                                                                                             |
| Chat stops answering mid-month                          | You used the monthly allowance. Code suggestions still work; credits reset on the first. Use another free tool for now.                                                 |
| I am not sure what I did                                | Ask in class, in office hours, or post in the course discussion. Bring the email GitHub sent you.                                                                       |

## Links in one place

| **Purpose**                                 | **Link**                                                                                                                                                                                       |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create a GitHub account                     | [github.com/signup](https://github.com/signup)                                                                                                                                          |
| Copilot chat on the web (Step A and Step D) | [github.com/copilot](https://github.com/copilot)                                                                                                                                        |
| Add and verify your DU email (Step B)       | [github.com/settings/emails](https://github.com/settings/emails)                                                                                                                        |
| Apply to GitHub Education (Step B and C)    | [github.com/settings/education/benefits](https://github.com/settings/education/benefits)                                                                                                |
| Copilot settings and plan name (Step C)     | [github.com/settings/copilot](https://github.com/settings/copilot)                                                                                                                      |
| GitHub Education application help           | [GitHub Docs: Apply to GitHub Education as a student](https://docs.github.com/en/education/about-github-education/github-education-for-students/apply-to-github-education-as-a-student) |
| Copilot Student instructions from GitHub    | [GitHub Docs: Access GitHub Copilot for free as a student](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students)              |
| Visual Studio Code download (Step D)        | [code.visualstudio.com](https://code.visualstudio.com)                                                                                                                                  |
| GitHub Support                              | [support.github.com](https://support.github.com)                                                                                                                                        |

*Details in this guide reflect GitHub's program as of September 2026. GitHub changes its free plans often; if a screen does not match, the links above go to GitHub's own current instructions.*
