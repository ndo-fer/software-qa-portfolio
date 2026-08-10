# QA Portfolio Execution Playbook
## Fernando Michael Panjaitan
### Build-from-Zero Guide for a Public, Interview-Ready QA Portfolio

> **Purpose of this document**
>
> This playbook is designed to help you build a QA portfolio **from zero on your local machine**, based on the competencies you have actually practiced during internships, while keeping all company data, source code, credentials, screenshots, business rules, and internal documents private.
>
> The goal is **not** to recreate your internship projects. The goal is to recreate the **QA and system-analysis methods** you used in a clean-room environment using public applications, dummy data, and independently written artifacts.

---

# 0. Final Portfolio Target

Your public QA portfolio will eventually contain three main projects and one optional project.

```text
qa-portfolio/
│
├── README.md
├── 01-ecommerce-qa-case-study/
│   ├── README.md
│   ├── docs/
│   │   ├── 01-product-requirements.md
│   │   ├── 02-test-plan.md
│   │   ├── 03-test-scenarios.xlsx
│   │   ├── 04-test-cases.xlsx
│   │   ├── 05-exploratory-notes.md
│   │   ├── 06-bug-reports.xlsx
│   │   ├── 07-test-execution-report.md
│   │   └── 08-regression-scope.md
│   ├── automation/
│   │   ├── cypress/
│   │   ├── package.json
│   │   ├── cypress.config.ts
│   │   └── README.md
│   └── evidence/
│       ├── screenshots/
│       └── reports/
│
├── 02-legacy-erp-analysis-case-study/
│   ├── README.md
│   ├── 01-project-context.md
│   ├── 02-domain-learning-notes.md
│   ├── 03-legacy-feature-inventory.xlsx
│   ├── 04-business-flow-reconstruction.md
│   ├── 05-legacy-to-web-mapping.xlsx
│   ├── 06-scope-and-open-questions.xlsx
│   ├── 07-mini-srd.md
│   ├── 08-requirement-register.xlsx
│   ├── 09-traceability-matrix.xlsx
│   └── 10-selected-test-cases.xlsx
│
├── 03-api-testing-case-study/
│   ├── README.md
│   ├── docs/
│   │   ├── api-test-plan.md
│   │   ├── api-test-cases.xlsx
│   │   └── execution-summary.md
│   ├── postman/
│   │   ├── collection.json
│   │   └── environment.example.json
│   └── evidence/
│       └── reports/
│
└── 04-selenium-case-study/        # optional
    ├── README.md
    ├── tests/
    ├── pages/
    ├── test-data/
    └── reports/
```

The portfolio should demonstrate the following competency chain:

```text
Requirement
    ↓
Requirement Analysis
    ↓
Risk Identification
    ↓
Test Scenario Design
    ↓
Test Case Design
    ↓
Manual / Exploratory Execution
    ↓
Defect Reporting
    ↓
Retesting
    ↓
Regression
    ↓
Automation Candidate Selection
    ↓
Automation Implementation
    ↓
Execution Reporting
```

For the ERP project, add another chain:

```text
Limited Initial Documentation
    ↓
Domain Familiarization
    ↓
Legacy System Exploration
    ↓
Feature Inventory
    ↓
Business Flow Reconstruction
    ↓
Legacy-to-Web Mapping
    ↓
Scope / Open Questions
    ↓
Requirement Documentation
    ↓
Test Derivation
```

---

# 1. Core Principle: Clean-Room Portfolio

This portfolio must be **public-safe**.

You are allowed to reproduce:

- testing methodology;
- generic software flows;
- test-design techniques;
- folder architecture you personally understand;
- Page Object Model concepts;
- regression strategy;
- general e-commerce behavior;
- general ERP concepts;
- generic purchasing, sales, inventory, authentication, checkout, and payment workflows;
- dummy bugs that you independently reproduce on public/demo systems;
- lessons learned from your professional experience.

You must **not** publish:

- company source code;
- code copied from internship repositories;
- actual internal screenshots;
- credentials;
- access tokens;
- production/staging URLs not intended for public use;
- real phone numbers or customer information;
- internal Trello/Jira exports;
- private test cases;
- internal SRD/proposals;
- proprietary business rules;
- exact company architecture;
- database dumps;
- private API endpoints;
- private test reports;
- names of internal developers or stakeholders;
- unpublished company defects.

## 1.1 Transformation Rule

Whenever you want to use an internship experience:

```text
REAL EXPERIENCE
↓
Extract the QA competency
↓
Remove company-specific information
↓
Create an independent dummy/public scenario
↓
Re-execute the method yourself
↓
Publish only the new artifact
```

Example:

```text
Real experience:
Testing product variants during reorder.

Do NOT publish:
Exact company bug, screenshots, IDs, product names, or internal rule.

Public-safe reconstruction:
A demo store contains the same product in Size M and Size L.
Create a test case verifying that "Buy Again" preserves both variants independently.
```

---

# 2. Tools to Install

You can build almost everything locally with free tools.

## Required

- Git
- GitHub account
- Visual Studio Code
- Node.js LTS
- npm
- Cypress
- Microsoft Excel / Google Sheets / LibreOffice for artifact creation
- Postman

## Optional

- Java
- Selenium
- Maven or Gradle
- GitHub Desktop
- draw.io
- Mermaid
- Mochawesome
- Newman

## Verify installation

Run:

```bash
git --version
node --version
npm --version
```

Later:

```bash
npx cypress --version
```

For Newman:

```bash
npm install -g newman
newman --version
```

---

# 3. Create the Main Local Repository and Connect It to GitHub

This portfolio should be developed locally first, but the final working model is:

```text
Local workspace
    ↓
Git repository
    ↓
Meaningful commits
    ↓
GitHub remote repository
    ↓
Public reviewable portfolio
    ↓
QA Lead review from repository link
```

The repository history is part of the evidence. Do not wait until the entire portfolio is finished and then upload everything in one commit.

## 3.1 Choose a Local Workspace

Example on Windows:

```text
D:\Portfolio\
```

Open PowerShell / Terminal:

```bash
cd D:\Portfolio
mkdir qa-portfolio
cd qa-portfolio
```

## 3.2 Configure Git Identity

Check whether Git already knows your identity:

```bash
git config --global user.name
git config --global user.email
```

If empty, configure it:

```bash
git config --global user.name "Fernando Michael Panjaitan"
git config --global user.email "YOUR_GITHUB_EMAIL"
```

Use an email you are comfortable associating with GitHub commits. If you use GitHub's private/no-reply email feature, use that address instead.

## 3.3 Initialize the Repository

```bash
git init
```

Immediately rename the default branch to `main`:

```bash
git branch -M main
```

Create the initial structure:

```text
README.md
.gitignore
01-ecommerce-qa-case-study/
02-legacy-erp-analysis-case-study/
03-api-testing-case-study/
04-selenium-case-study/
```

Suggested shell commands:

```bash
mkdir 01-ecommerce-qa-case-study
mkdir 02-legacy-erp-analysis-case-study
mkdir 03-api-testing-case-study
mkdir 04-selenium-case-study
```

If an empty directory must be tracked by Git, create a `.gitkeep` file inside it or wait until the directory contains a real artifact.

## 3.4 Create `.gitignore` Before Adding Files

Create:

```text
.gitignore
```

Recommended initial content:

```gitignore
# Dependencies
node_modules/

# Environment / secrets
.env
.env.*
!.env.example

# Cypress generated artifacts
cypress/videos/
cypress/downloads/

# OS / editor noise
.DS_Store
Thumbs.db
.vscode/settings.json

# Temporary files
*.tmp
*.log
```

Do not blindly ignore all reports. Representative public-safe reports are useful portfolio evidence. Decide intentionally which generated reports you want to retain.

## 3.5 First Local Commit

Check status:

```bash
git status
```

Stage files:

```bash
git add README.md .gitignore
```

Commit:

```bash
git commit -m "chore: initialize QA portfolio"
```

Verify:

```bash
git log --oneline
```

Expected pattern:

```text
abc1234 chore: initialize QA portfolio
```

## 3.6 Create the GitHub Repository

On GitHub, create a new repository.

Recommended repository name:

```text
qa-portfolio
```

Recommended initial state:

```text
Visibility: Private while setup is incomplete, or Public if you are comfortable
Initialize with README: No
Add .gitignore: No
Add license: Optional / No for now
```

Why no GitHub-generated README?

Because the local repository already contains the canonical README. This avoids unnecessary initial merge conflicts.

## 3.7 Connect Local Git to GitHub

Copy the repository URL from GitHub.

HTTPS example:

```text
https://github.com/YOUR_USERNAME/qa-portfolio.git
```

Add it as `origin`:

```bash
git remote add origin https://github.com/YOUR_USERNAME/qa-portfolio.git
```

Verify:

```bash
git remote -v
```

Expected:

```text
origin  https://github.com/YOUR_USERNAME/qa-portfolio.git (fetch)
origin  https://github.com/YOUR_USERNAME/qa-portfolio.git (push)
```

## 3.8 First Push

```bash
git push -u origin main
```

The `-u` flag establishes `origin/main` as the upstream branch.

After this, ordinary pushes can use:

```bash
git push
```

## 3.9 Authentication Note

GitHub may ask you to authenticate through your browser, Git Credential Manager, SSH, or another supported Git authentication mechanism.

Do not put GitHub passwords, personal access tokens, or credentials inside:

```text
README
.env committed to Git
source code
shell scripts
screenshots
```

A token is a secret, not portfolio evidence.

## 3.10 Normal Daily Git Workflow

Before starting work:

```bash
git status
git pull --rebase
```

After completing one meaningful unit of work:

```bash
git status
git diff
git add <specific-files>
git commit -m "meaningful commit message"
git push
```

Prefer staging specific files while learning:

```bash
git add 01-ecommerce-qa-case-study/docs/01-product-requirements.md
```

rather than blindly using:

```bash
git add .
```

This forces you to inspect what you are publishing.

## 3.11 Commit Message Pattern

Recommended prefixes:

```text
chore: repository/setup work
docs: documentation
requirement: requirements and acceptance criteria
test: manual test design or test cases
bug: defect documentation
automation: UI automation
api: API testing
erp: ERP analysis artifact
refactor: code restructuring without changing intended behavior
fix: correction to portfolio code/artifact
```

Examples:

```text
chore: initialize QA portfolio
requirement: add ecommerce authentication requirements
test: add login exploratory session
test: add cart boundary scenarios
docs: add ecommerce test plan
bug: document cart quantity validation issue
automation: initialize Cypress TypeScript project
automation: add login page object
automation: add authenticated session command
automation: add checkout regression scenarios
erp: add legacy feature inventory
erp: add legacy-to-web mapping
api: add negative authentication tests
```

Avoid meaningless history:

```text
update
final
final2
fix
fix again
latest
asdf
```

## 3.12 One Commit Should Represent One Coherent Change

Good:

```text
test: add authentication negative cases
```

Bad:

```text
update everything
```

A recruiter may never inspect every commit, but clean history supports the impression that you work systematically.

## 3.13 Branching Strategy for This Portfolio

For the early stages, keep it simple:

```text
main
```

You do not need GitFlow just to demonstrate that you know branches exist.

Once the repository becomes larger, optional feature branches can be used:

```bash
git checkout -b feature/cypress-cart-suite
```

After completion:

```bash
git checkout main
git merge feature/cypress-cart-suite
```

But only do this if you understand the workflow. Artificial branch complexity adds no portfolio value.

## 3.14 Private During Construction vs Public from the Beginning

Both are acceptable.

### Option A — Private During Construction

Recommended if:

- you are worried about accidentally committing confidential material;
- the repository is still messy;
- you want a privacy review before publication.

Workflow:

```text
Local
→ Private GitHub
→ content/security review
→ Public
```

### Option B — Public from the Beginning

Recommended if:

- the repository contains only synthetic/public-safe material;
- you want continuous external review;
- you are disciplined about secrets.

Workflow:

```text
Local
→ Public GitHub
→ send repository link for review at every sprint
```

## 3.15 Mandatory Pre-Push Safety Check

Before every important push, ask:

```text
Am I publishing any company artifact?
Am I publishing any credential?
Am I publishing a private URL?
Am I publishing a real customer/user identity?
Am I publishing internal screenshots?
Am I publishing copied internship source code?
Am I publishing a real API key/token?
Am I publishing an internal business rule that should remain private?
```

Then run:

```bash
git status
git diff --staged
```

Read the staged diff before pushing.

Do **not** push internship materials even temporarily with the intention of deleting them later. Git history can preserve earlier content.

## 3.16 Secret-Safe Configuration

Bad:

```ts
const username = "real.company.account@example.com"
const password = "CompanyPassword123"
```

Better:

```text
.env              # ignored
.env.example      # public template
```

`.env.example`:

```text
TEST_USERNAME=replace_me
TEST_PASSWORD=replace_me
```

README:

```text
Copy `.env.example` to `.env` and provide your own demo credentials.
```

## 3.17 Before Making the Repository Public

Complete this checklist:

- [ ] no internship source code;
- [ ] no real production/staging credentials;
- [ ] no internal Trello/Jira exports;
- [ ] no internal SRD/proposal files;
- [ ] no employee/customer personal data;
- [ ] no private API endpoint;
- [ ] no hidden token inside JSON fixtures;
- [ ] no screenshots exposing private information;
- [ ] `.gitignore` reviewed;
- [ ] README contains a confidentiality disclaimer;
- [ ] every claim in README is supported by public artifacts;
- [ ] install/run instructions work.

## 3.18 Fresh-Clone Validation Before Public Release

This is important.

Do not validate only from the directory where you developed the project, because hidden local files may make it appear to work.

Create a completely separate folder:

```bash
cd D:\Portfolio
mkdir portfolio-validation
cd portfolio-validation
git clone https://github.com/YOUR_USERNAME/qa-portfolio.git
cd qa-portfolio
```

Then follow your own README as if you were a recruiter/developer who has never seen the project.

For Cypress later:

```bash
cd 01-ecommerce-qa-case-study/automation
npm install
npx cypress run
```

Ask:

```text
Can a stranger understand the project?
Can a stranger install it?
Can a stranger run it?
Are any undocumented local files required?
Do commands in README actually work?
```

If the fresh clone fails, the portfolio is not done.

## 3.19 GitHub Link Review Workflow With ChatGPT

Once the repository is public, you may send only the repository link.

Example:

```text
https://github.com/YOUR_USERNAME/qa-portfolio
```

Recommended review request:

```text
Audit this public repository as my QA Lead.
Inspect the actual artifacts and automation code, not only the README.
Validate requirement-to-test traceability, test-design quality, defect
reasoning, Cypress architecture, assertions, selector quality, test data,
repository hygiene, reproducibility, and whether my public claims are
supported by evidence. Score it and block the next sprint if necessary.
```

The review model will be:

```text
Public GitHub repository
        ↓
Repository audit
        ↓
QA Lead score
        ↓
Required corrections
        ↓
You update locally
        ↓
Commit + push
        ↓
Re-review
```

## 3.20 Repository Publication Milestones

Suggested milestones:

```text
M0 — Repository initialized
M1 — Sprint 1 artifacts complete
M2 — Manual QA suite complete
M3 — Cypress automation complete
M4 — E-commerce project recruiter-ready
M5 — ERP case study complete
M6 — API case study complete
M7 — Final portfolio audit passed
```

Tagging releases is optional, but useful after major milestones:

```bash
git tag -a ecommerce-v1.0 -m "Complete ecommerce QA case study"
git push origin ecommerce-v1.0
```

Do not create releases for every tiny change.

## 3.21 What the Git Setup Is Supposed to Demonstrate

Git is not included merely because recruiters expect the word `Git`.

The repository should prove that you can:

```text
maintain a structured project;
track meaningful changes;
avoid publishing secrets;
write reproducible setup instructions;
separate source, data, evidence, and generated artifacts;
collaborate through a conventional version-control workflow.
```

Do **not** push internal internship materials into this repository, even temporarily.

---


# 3A. Execution Governance — Human vs AI Coding Agent Responsibilities

This playbook may be executed with the help of a local AI coding agent, IDE agent, or coding assistant.

However, the AI agent is **not the owner of the QA reasoning**. The portfolio is intended to prove that **you** can reason as a QA engineer/system analyst. Therefore, the agent may accelerate setup, formatting, repetitive implementation, and validation, but it must not silently make the core QA decisions on your behalf.

The operating model is:

```text
PLAYBOOK
    ↓
AI AGENT handles setup / mechanical work
    ↓
HUMAN handles QA judgment / analysis
    ↓
AI AGENT may challenge, validate, or format
    ↓
HUMAN makes the final decision
    ↓
Artifact is committed
```

The goal is not to avoid AI. The goal is to ensure that every portfolio artifact remains **interview-defensible by you**.

---

## 3A.1 Three Levels of Agent Permission

Every task in this portfolio falls into one of three modes.

### MODE A — Agent May Execute Independently

The agent may perform these tasks without asking for approval every time:

```text
create folders;
initialize Git;
create .gitignore;
create empty files;
create document/spreadsheet skeletons;
format Markdown;
install project dependencies;
create package.json;
configure TypeScript;
configure Cypress after the automation sprint starts;
create boilerplate Page Object classes;
run tests;
run linters;
collect command output;
check file paths;
check naming consistency;
check broken Markdown links;
check Git status;
show diffs;
prepare Git commands;
validate that required files exist;
summarize implementation status.
```

The agent can also transform **your already-made QA decision** into a cleaner artifact.

Example:

```text
YOU:
Severity = MAJOR because the user cannot complete checkout,
but there is a workaround through another payment method.

AGENT:
Formats that reasoning into the bug-report spreadsheet.
```

That is allowed.

### MODE B — Agent May Assist, but Human Must Decide

The agent may analyze, question, suggest alternatives, or identify missing considerations, but **you make the final decision**.

Examples:

```text
requirement wording;
test scope;
risk classification;
test priority;
test-design technique;
edge cases;
defect classification;
severity;
priority;
regression scope;
automation candidate selection;
business-rule interpretation;
ERP legacy-to-web mapping decision;
open-question formulation;
requirement acceptance criteria.
```

Correct workflow:

```text
YOU make first attempt
        ↓
AGENT reviews/challenges it
        ↓
YOU accept/reject/revise
        ↓
AGENT records the final decision
```

The agent must not quietly convert its recommendation into the official artifact without your approval.

### MODE C — Agent Must Stop and Ask the Human

The agent must stop whenever continuing would require inventing observations, evidence, or decisions that only the tester can establish.

Examples:

```text
choosing what actually happened during exploratory testing;
claiming a defect was observed;
deciding an unknown product behavior is expected;
inventing Actual Result;
inventing PASS / FAIL results;
inventing browser/device execution;
inventing defect evidence;
inventing interview/internship facts;
inventing stakeholder confirmation;
inventing performance numbers;
inventing production impact;
inventing security impact;
claiming a requirement is confirmed when it is only assumed.
```

The following six questions are explicit **human checkpoints**:

```text
1. What requirements should exist?
2. What is a risk?
3. What edge case did I miss?
4. Is this actually a defect?
5. What severity should this have?
6. What should be automated?
```

The agent may help you reason about these questions, but it must not answer them silently and continue as though the answer came from you.

---

## 3A.2 Human Checkpoint 1 — “What Requirements Should Exist?”

The agent may create the requirement template, numbering scheme, or examples.

You must determine or approve:

```text
what user capability is actually being specified;
what behavior is mandatory;
what behavior is optional;
what assumption is being made;
what is based on observation;
what is deliberately out of scope.
```

Recommended workflow:

```text
1. Observe/study the public demo system.
2. Write your own first-pass requirement.
3. Mark uncertainty explicitly.
4. Ask the agent to review testability and ambiguity.
5. Revise it yourself.
```

Do not allow the agent to generate 25 requirements and automatically treat all of them as product truth.

Use labels when needed:

```text
OBSERVED
ASSUMED
DERIVED FOR PORTFOLIO
TBD
```

---

## 3A.3 Human Checkpoint 2 — “What Is a Risk?”

A risk must be tied to a plausible consequence.

You decide:

```text
what can fail;
who is affected;
how the business/user is affected;
how likely the problem is;
whether the risk belongs in the current test scope.
```

The agent may challenge your analysis.

Example:

```text
Weak:
"Login is high risk because login is important."

Better:
"Authentication is high risk because failure blocks registered users from
accessing cart, checkout, and order-history functions that depend on an
authenticated session."
```

The portfolio should demonstrate **reasoned risk**, not labels generated automatically.

---

## 3A.4 Human Checkpoint 3 — “What Edge Case Did I Miss?”

You must first attempt to identify edge cases using the test-design techniques in this playbook.

Think about:

```text
boundaries;
empty states;
duplicate actions;
state changes;
refresh/back navigation;
session expiry;
different variants;
minimum/maximum quantities;
invalid combinations;
partial completion;
interrupted flows;
cross-module dependencies.
```

After your first attempt, the agent may act as a reviewer:

```text
Challenge my current test coverage and identify categories I may have
missed. Do not add them to the official spreadsheet until I approve them.
```

This distinction is important. The goal is to train your own QA pattern recognition.

---

## 3A.5 Human Checkpoint 4 — “Is This Actually a Defect?”

A surprising behavior is **not automatically a defect**.

Before recording a real defect, check:

```text
Is the behavior reproducible?
Does it contradict a stated requirement?
Does it contradict a stable observed product rule?
Does it prevent or distort the intended user flow?
Could it be expected behavior?
Could the test data be wrong?
Could the environment be unstable?
Could the tester have misunderstood the feature?
Is more clarification required?
```

Use one of these classifications:

```text
CONFIRMED DEFECT
Behavior clearly contradicts supported expected behavior.

POTENTIAL DEFECT — NEEDS CLARIFICATION
Behavior is suspicious, but expected behavior is not sufficiently established.

ENVIRONMENT / TEST DATA ISSUE
Failure is caused by environment or data rather than product behavior.

NOT A DEFECT
Behavior is consistent with the supported requirement.

SIMULATED DEFECT
Intentionally created portfolio example that was not genuinely discovered.
It must be labeled clearly.
```

The agent must never convert `POTENTIAL DEFECT` into `CONFIRMED DEFECT` by assumption.

---

## 3A.6 Human Checkpoint 5 — “What Severity Should This Have?”

Severity is based primarily on **impact**, not how annoying the bug looks.

You make the severity decision.

Consider:

```text
Is a critical business flow blocked?
Is there data loss or corruption?
Is there a security/privacy consequence?
How many users/functions are affected?
Is there a workaround?
Does the application remain usable?
Is the issue cosmetic only?
```

Use the portfolio scale:

```text
CRITICAL
System/core transaction unusable, serious security/data integrity risk,
or no reasonable workaround.

MAJOR
Important functionality fails or produces materially incorrect behavior,
with significant user/business impact.

MINOR
Limited functional or UI problem with relatively low impact or a practical workaround.

SUGGESTION
Improvement or usability recommendation rather than a confirmed functional defect.
```

The agent may ask questions such as:

```text
Can the user still complete the transaction?
Is data corrupted?
Is there a workaround?
Does this affect all users or a narrow condition?
```

But **you select the final severity** and should be able to defend it in an interview.

---

## 3A.7 Human Checkpoint 6 — “What Should Be Automated?”

Automation is a strategic selection problem.

Do not automate a test merely because it can technically be automated.

You decide based on:

```text
business criticality;
execution frequency;
regression value;
determinism;
test-data controllability;
external dependencies;
maintenance cost;
UI stability;
manual observation value.
```

A good candidate is usually:

```text
high-value
+ repetitive
+ deterministic
+ stable enough
+ useful in regression
```

A poor candidate may be:

```text
visual-only;
highly exploratory;
dependent on manual hardware interaction;
unstable third-party behavior;
rarely executed;
expensive to maintain relative to its value.
```

The agent may calculate or display the candidate score after **you** provide the reasoning inputs.

---

## 3A.8 The Agent Must Never Fabricate Test Execution

This rule is absolute.

The agent must never fill these fields without real execution evidence:

```text
Actual Result
PASS
FAIL
BLOCKED
Retest Result
Browser Result
Device Result
Execution Date
Defect Reproduction
Screenshot Evidence
Console Evidence
Network Evidence
```

If execution has not occurred, use:

```text
NOT RUN
```

or leave the field blank according to the artifact convention.

Generated example data must be labeled:

```text
EXAMPLE
SIMULATED
DUMMY
```

---

## 3A.9 The Agent Must Distinguish Observation, Assumption, and Requirement

Use this evidence hierarchy:

```text
CONFIRMED REQUIREMENT
Supported by explicit public specification or human-confirmed project decision.

OBSERVED BEHAVIOR
Directly observed during exploration/execution.

PORTFOLIO REQUIREMENT
A requirement intentionally defined by you for the clean-room case study.

ASSUMPTION
A temporary interpretation used because information is incomplete.

OPEN QUESTION
A decision that still requires clarification.
```

Never silently upgrade:

```text
ASSUMPTION → CONFIRMED REQUIREMENT
```

or:

```text
OBSERVED BEHAVIOR → CORRECT BUSINESS RULE
```

Observation proves what the current system does, not necessarily what it **should** do.

---

## 3A.10 AI Review Is Allowed to Be Adversarial

The agent should not merely agree with your artifacts.

After you complete a first draft, you may instruct it to challenge you.

Useful prompts:

```text
Review this as a strict QA Lead.
Do not rewrite it yet.
Identify unsupported assumptions, missing negative cases, weak expected
results, duplicated scenarios, and anything that is not actually testable.
```

```text
Challenge my severity choice.
Ask me the impact/workaround questions required to defend or change it.
Do not select the final severity for me.
```

```text
Review my automation candidates.
For every Yes, challenge whether the test is repetitive, deterministic,
business-critical, and maintainable.
```

```text
Find gaps in my coverage by category.
Do not automatically add test cases. Return review comments only.
```

---

## 3A.11 Required Agent Stop Message

When a human decision is needed, the preferred behavior is:

```text
HUMAN DECISION REQUIRED

Artifact:
<file>

Decision:
<what must be decided>

Current evidence:
<what is actually known>

Unknown:
<what cannot be established automatically>

Your task:
<what the user should answer/do>

I will not finalize this artifact until you decide.
```

This makes agent behavior predictable.

---

## 3A.12 Sprint Boundary Rule

The agent must execute **only the sprint explicitly requested**.

If instructed:

```text
Execute Sprint 1.
```

it must not:

```text
initialize Cypress;
write the complete automation suite;
generate final bug statistics;
complete the ERP project;
start the API project.
```

At the end of the sprint, it must stop and report:

```text
Completed
Pending human decisions
Files created/modified
Tests actually executed
Git status
Recommended next checkpoint
```

Only proceed after human approval/review.

---

## 3A.13 Local Coding Agent Kickoff Prompt

After placing this playbook in the root of the repository, use the following prompt as the standard kickoff instruction:

```text
Read QA_Portfolio_Execution_Playbook.md completely before making changes.

We are building this QA portfolio from zero.

Execute ONLY the sprint I explicitly request.

Follow Section 3A: Execution Governance — Human vs AI Coding Agent
Responsibilities.

Rules:
1. Do not skip ahead to a later sprint.
2. Do not invent requirements, observations, defects, execution results,
   severity decisions, business rules, or internship facts.
3. You may create repository structure, templates, boilerplate, setup,
   formatting, dependencies, and validation automatically when allowed by
   Section 3A.
4. For QA judgment, require my first attempt or explicit approval.
5. When a Human Checkpoint is reached, stop and show HUMAN DECISION REQUIRED.
6. Do not mark any test PASS/FAIL unless it was actually executed and the
   evidence supports that result.
7. Do not use confidential company information.
8. Do not copy internal source code, screenshots, credentials, documents,
   endpoints, or proprietary business rules.
9. Do not complete QA reasoning artifacts on my behalf merely to finish the sprint.
10. At the end of the requested sprint, stop and report:
    - completed tasks;
    - pending human decisions;
    - files created/modified;
    - tests actually executed;
    - Git status;
    - whether the sprint Definition of Done is satisfied.

If any instruction conflicts with the confidentiality or human-judgment rules,
stop and ask me before proceeding.
```

---

## 3A.14 Recommended First Command to the Agent

For the beginning of this portfolio:

```text
Execute Sprint 1 from QA_Portfolio_Execution_Playbook.md.

Start with repository/Git setup and the Project 1 skeleton.

Follow Section 3A strictly.

Do not start Cypress.

When we reach target-application selection or any QA reasoning checkpoint,
stop and ask me instead of deciding automatically.
```

---

## 3A.15 What You Should Personally Be Able to Explain

Before an artifact is considered portfolio-ready, you should be able to answer:

```text
Why does this requirement exist?
Why is this scenario important?
Which test-design technique produced this case?
Why is this an edge case?
What evidence makes this a defect?
Why did you choose this severity?
What is the regression impact?
Why did you automate this case?
Why did you leave this case manual?
What assumption did you make?
What would you clarify with a PM/BA/user?
```

If you cannot explain an artifact without reading an AI-generated answer, the artifact is **not finished**.

---

## 3A.16 Governance Definition of Done

Before publishing a project, verify:

- [ ] core QA judgments were made or explicitly approved by you;
- [ ] no execution results were fabricated;
- [ ] assumptions and open questions are labeled;
- [ ] genuine vs simulated defects are clearly distinguished;
- [ ] severity choices have defensible impact reasoning;
- [ ] automation candidates have explicit selection reasoning;
- [ ] AI-generated boilerplate was reviewed and understood;
- [ ] all public claims can be defended from repository evidence;
- [ ] you can explain every important artifact in an interview.

---

# 4. Main README

Create:

```text
qa-portfolio/README.md
```

Recommended initial structure:

```md
# Fernando Michael Panjaitan — QA Portfolio

Quality Assurance portfolio demonstrating practical work in:

- manual functional testing;
- exploratory testing;
- test scenario and test case design;
- regression testing;
- defect reporting;
- Cypress automation with TypeScript;
- Page Object Model;
- API testing;
- requirement analysis;
- legacy ERP requirement reconstruction.

## Portfolio Projects

### 1. E-Commerce QA Case Study
Manual testing, regression planning, defect reporting, and Cypress automation.

### 2. Legacy ERP Migration Analysis
Legacy-system exploration, business-flow reconstruction, feature mapping,
requirement documentation, and test derivation.

### 3. REST API Testing
Postman-based positive, negative, validation, and CRUD testing.

### 4. Selenium Case Study
Optional secondary UI automation project.

## Core Tools

Cypress | Selenium | Postman | TypeScript | JavaScript | Git | SQL

## Disclaimer

All portfolio projects are independently recreated using public or dummy
systems and synthetic test data. No confidential company source code,
credentials, internal documentation, or proprietary business information
is included.
```

Do not over-design it yet.

The goal is **substance first**.

---

# 5. PROJECT 1 — E-Commerce QA Case Study

This is your **primary QA portfolio project**.

It should demonstrate:

- requirement comprehension;
- exploratory testing;
- modular test design;
- positive and negative cases;
- defect discovery;
- severity reasoning;
- retest and regression;
- Cypress architecture;
- TypeScript;
- POM;
- fixtures;
- reusable commands;
- session management;
- reports;
- cross-browser strategy;
- responsive strategy.

---

# 6. Project 1 Step 1 — Choose the Public Test Application

Use a public demo application intended for testing.

Possible categories:

- demo e-commerce website;
- automation practice store;
- open-source storefront deployed publicly.

Criteria:

- registration/login;
- products;
- search;
- product detail;
- cart;
- quantity;
- checkout;
- preferably account/profile;
- stable enough for repeat testing;
- does not require using real money.

Do **not** choose a website whose terms prohibit automated testing.

Record your selected target inside:

```text
01-ecommerce-qa-case-study/README.md
```

Do not start Cypress yet.

---

# 7. Project 1 Step 2 — Create Product Requirements

Create:

```text
docs/01-product-requirements.md
```

This is **not** copied from the demo app.

You write simplified requirements yourself.

Example structure:

```md
# Product Requirements

## Product
DemoCommerce

## Objective
Allow registered users to discover products and complete a purchase flow.

## User Roles
- Guest
- Registered User

## Modules
1. Authentication
2. Navigation
3. Product Search
4. Product Detail
5. Cart
6. Checkout
7. Order

## Functional Requirements

### AUTH-001 Login
A registered user shall be able to log in using valid credentials.

### AUTH-002 Invalid Login
The system shall reject invalid credentials with a clear user-facing error.

### PROD-001 Search
A user shall be able to search products using product keywords.

### CART-001 Add to Cart
A user shall be able to add an available product to the shopping cart.

### CART-002 Variant Preservation
When multiple variants of the same product are added, each variant shall
remain a separate cart line.

### CART-003 Last Item Removal
Removing the final item shall result in an empty-cart state without an
application error.

### CHK-001 Checkout
A registered user with at least one cart item shall be able to proceed to
checkout.

### CHK-002 Required Address
Checkout shall not proceed if mandatory delivery information is missing.
```

Target:

- approximately 15–25 functional requirements;
- enough to build meaningful test coverage;
- not hundreds.

---

# 8. Project 1 Step 3 — Exploratory Testing Before Formal Test Cases

You normally used:

```text
read requirement
→ exploratory
→ formalize test cases
→ testing
```

Maintain that.

Create:

```text
docs/05-exploratory-notes.md
```

Use a session-based format.

```md
# Exploratory Testing Notes

## Session E-001

### Charter
Explore login behavior for valid, invalid, and expired-session conditions.

### Duration
30 minutes

### Areas
- login
- validation
- session
- error messaging

### Observations
1. ...
2. ...
3. ...

### Risks
- user may not understand invalid login message;
- session expiry may redirect without explanation.

### Candidate Test Cases
- login valid;
- invalid password;
- unknown account;
- blank field;
- expired session.

### Possible Defects
- ...
```

Do not worry if the app has no real bugs.

The goal is to show your analysis process.

---

# 9. Project 1 Step 4 — Build a Test Plan

Create:

```text
docs/02-test-plan.md
```

Required sections:

```md
# Test Plan

## 1. Objective

## 2. Product Under Test

## 3. Scope

### In Scope
- authentication
- navigation
- product search
- product detail
- cart
- checkout

### Out of Scope
- real payment settlement
- production infrastructure
- load testing
- penetration testing

## 4. Test Types
- functional
- exploratory
- negative
- regression
- cross-browser
- responsive

## 5. Test Environment

## 6. Browsers
- Chrome
- Firefox
- optional Edge

## 7. Devices / Viewports
- desktop
- tablet
- mobile

## 8. Test Data

## 9. Entry Criteria

## 10. Exit Criteria

## 11. Defect Classification

## 12. Risks

## 13. Deliverables
```

### Suggested Entry Criteria

```text
Application reachable
Core features available
Dummy test account prepared
No known environment outage blocking execution
```

### Suggested Exit Criteria

```text
All critical-path scenarios executed
No unresolved blocker defect
Critical and major defects documented
Regression scope executed after fixes
Automation suite passes for selected stable flows
```

---

# 10. Project 1 Step 5 — Build Test Scenarios

Create spreadsheet:

```text
docs/03-test-scenarios.xlsx
```

Columns:

| Scenario ID | Module | Submodule | Scenario | Type | Priority | Automation Candidate |
|---|---|---|---|---|---|---|

Example:

| Scenario ID | Module | Submodule | Scenario | Type | Priority | Automation Candidate |
|---|---|---|---|---|---|---|
| TS-AUTH-001 | Authentication | Login | Login with valid account | Positive | High | Yes |
| TS-AUTH-002 | Authentication | Login | Login with invalid credentials | Negative | High | Yes |
| TS-AUTH-003 | Authentication | Session | Access after session expiry | State | High | Maybe |
| TS-CART-001 | Cart | Add Item | Add product from listing | Positive | High | Yes |
| TS-CART-002 | Cart | Variant | Add same product with different variant | Business Rule | High | Yes |
| TS-CART-003 | Cart | Remove | Remove final cart item | Edge | High | Yes |

Target:

- 30–50 scenarios;
- do not inflate the number artificially.

---

# 11. Project 1 Step 6 — Build Detailed Test Cases

Create:

```text
docs/04-test-cases.xlsx
```

Recommended columns:

| Test Case ID | Requirement ID | Module | Scenario | Preconditions | Test Data | Steps | Expected Result | Actual Result | Status | Severity if Failed | Automation |
|---|---|---|---|---|---|---|---|---|---|---|---|

Example:

```text
Test Case ID: TC-CART-007
Requirement: CART-003
Module: Cart
Scenario: Remove final cart item
Precondition:
- User logged in
- Cart contains exactly one item

Steps:
1. Open cart
2. Click remove
3. Confirm removal if required

Expected:
- item removed;
- empty-cart UI appears;
- cart counter becomes zero;
- page remains usable;
- no console error caused by the action.
```

Target:

- 50–80 high-quality test cases.

Do not target 200 unless the system truly needs them.

---

# 12. Test Design Techniques to Deliberately Demonstrate

Recruiters should see that your cases are not random.

Mark some test cases with a `Technique` column.

Use:

## Equivalence Partitioning

Example password:

```text
valid password
invalid password
blank password
```

## Boundary Value Analysis

Example quantity:

```text
minimum allowed
minimum - 1
maximum allowed
maximum + 1
```

## State Transition

Example:

```text
Logged Out
→ Logged In
→ Session Expired
→ Re-authentication
```

## Decision Table

Example:

```text
User Logged In?
Cart Has Item?
Address Complete?
Payment Selected?
→ Checkout Allowed?
```

## Error Guessing

Based on your experience:

- double click submit;
- reload during checkout;
- delete final cart item;
- same product with multiple variants;
- stale session;
- back button after payment;
- duplicate order;
- empty search.

---

# 13. Project 1 Step 7 — Manual Execution

Run your test cases.

Populate:

```text
Actual Result
Status
Evidence
```

Recommended statuses:

```text
PASS
FAIL
BLOCKED
NOT RUN
```

Do not fake defects.

If the demo app genuinely fails, report it.

If you need a demonstration defect that is not genuine, label it:

```text
SIMULATED DEFECT
```

---

# 14. Project 1 Step 8 — Bug Reporting

Create:

```text
docs/06-bug-reports.xlsx
```

Columns:

| Bug ID | Title | Module | Environment | Preconditions | Steps to Reproduce | Actual Result | Expected Result | Severity | Priority | Evidence | Status | Retest Result |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

Severity model:

```text
CRITICAL
Application unusable, security/data-loss risk, or core business transaction impossible.

MAJOR
Important feature broken with significant user/business impact.

MINOR
Limited functional/UI issue with workaround or low business impact.

SUGGESTION
Improvement, consistency, usability, or non-defect recommendation.
```

Use severity based on **impact**, not emotion.

---

# 15. Bug Types Worth Seeking

Do not intentionally break unauthorized systems.

On a demo application, inspect:

- login error feedback;
- session expiry;
- cart synchronization;
- variant handling;
- price calculation;
- discount calculation;
- item removal;
- duplicate action;
- search empty state;
- sort order;
- responsive layout;
- stale UI;
- missing validation;
- checkout validation;
- redirect behavior;
- browser console;
- browser network failures.

The bug concepts are inspired by competencies you have handled professionally, but all public evidence must come from the independent demo system.

---

# 16. Project 1 Step 9 — Retest and Regression

For a fixed defect:

```text
1. reproduce old defect;
2. confirm it no longer occurs;
3. run closely related cases;
4. run critical-path regression if impact is broad.
```

Create:

```text
docs/08-regression-scope.md
```

Example:

```md
# Regression Scope

## Critical Path

1. Login
2. Search product
3. Open product detail
4. Add product
5. Open cart
6. Change quantity
7. Checkout
8. Order confirmation

## Trigger-Based Regression

### Authentication Change
Run:
- AUTH suite
- profile access
- checkout login dependency

### Cart Change
Run:
- add item
- variant
- quantity
- remove
- checkout summary

### Checkout Change
Run:
- cart
- address
- shipping
- payment selection
- order confirmation
```

---

# 17. Project 1 Step 10 — Select Automation Candidates

Do not automate everything.

Score cases against:

| Criterion | Low | Medium | High |
|---|---|---|---|
| Repetition | | | |
| Business Criticality | | | |
| Determinism | | | |
| Regression Frequency | | | |
| Setup Cost | | | |
| Maintenance Cost | | | |

Good automation targets:

- login;
- search;
- navigation;
- product detail;
- add-to-cart;
- quantity;
- checkout core flow.

Manual-first targets:

- visual polish;
- exploratory behavior;
- unusual UX;
- constantly changing UI;
- cases depending heavily on external manual interaction.

---

# 18. Project 1 Step 11 — Create Cypress Project from Zero

Go to:

```bash
cd 01-ecommerce-qa-case-study
mkdir automation
cd automation
npm init -y
npm install cypress --save-dev
npx cypress open
```

Install TypeScript if needed:

```bash
npm install typescript --save-dev
```

Install Mochawesome reporter:

```bash
npm install cypress-mochawesome-reporter --save-dev
```

Target architecture:

```text
automation/
├── cypress/
│   ├── e2e/
│   │   ├── auth/
│   │   │   └── login.cy.ts
│   │   ├── navigation/
│   │   │   └── navigation.cy.ts
│   │   ├── product/
│   │   │   ├── search.cy.ts
│   │   │   └── product-detail.cy.ts
│   │   ├── cart/
│   │   │   └── cart.cy.ts
│   │   └── checkout/
│   │       └── checkout.cy.ts
│   ├── fixtures/
│   │   ├── users.json
│   │   └── products.json
│   ├── support/
│   │   ├── pages/
│   │   │   ├── LoginPage.ts
│   │   │   ├── HomePage.ts
│   │   │   ├── ProductPage.ts
│   │   │   ├── CartPage.ts
│   │   │   └── CheckoutPage.ts
│   │   ├── commands.ts
│   │   ├── e2e.ts
│   │   └── types.ts
│   └── screenshots/
├── cypress.config.ts
├── package.json
├── tsconfig.json
└── README.md
```

---

# 19. Cypress Coding Standards

## Page Object

Example conceptual structure:

```ts
class LoginPage {
  elements = {
    email: () => cy.get('[data-testid="email"]'),
    password: () => cy.get('[data-testid="password"]'),
    submit: () => cy.get('[data-testid="login-submit"]'),
    error: () => cy.get('[data-testid="login-error"]'),
  }

  visit() {
    cy.visit('/login')
  }

  login(email: string, password: string) {
    this.elements.email().type(email)
    this.elements.password().type(password)
    this.elements.submit().click()
  }
}

export default new LoginPage()
```

Prefer stable selectors:

```text
data-testid
data-cy
id
stable semantic attributes
```

Avoid selectors such as:

```text
:nth-child(5) > div > div > button
```

unless unavoidable.

---

# 20. Use Session Reuse Correctly

For authenticated regression tests, consider:

```ts
Cypress.Commands.add('login', () => {
  cy.session('demo-user', () => {
    // independent UI login
  })
})
```

But keep dedicated login tests that explicitly test the login UI.

This demonstrates the distinction:

```text
Testing authentication itself
≠
Repeated authentication setup for unrelated tests
```

---

# 21. Assertions to Demonstrate

Use a variety of meaningful assertions:

```text
URL
visibility
existence
text
attribute
enabled / disabled
list length
cart count
price
state
navigation
error message
```

Do not write tests that only:

```text
click
click
click
```

with no assertion.

---

# 22. Flaky-Test Discipline

Avoid arbitrary waits:

```ts
cy.wait(5000)
```

unless you can clearly justify them.

Prefer:

```text
element state;
intercepted request;
visible UI state;
route state;
specific timeout for known async behavior.
```

Document any unavoidable external dependency.

In README, include:

```md
## Known Automation Constraints

- External payment simulations are not fully controlled.
- Some demo data may change between sessions.
- Tests prefer deterministic assertions and avoid arbitrary sleeps.
```

---

# 23. Cross-Browser Plan

At minimum:

```bash
npx cypress run --browser chrome
npx cypress run --browser firefox
```

If supported:

```bash
npx cypress run --browser edge
```

Document Safari as manual if your environment cannot automate it.

Never claim Safari automation if you only tested Safari manually.

---

# 24. Responsive Plan

Manual:

```text
Android physical device
iPhone physical device, if available
browser responsive emulator
```

Automation sample:

```ts
cy.viewport(375, 812)
cy.viewport(768, 1024)
cy.viewport(1366, 768)
```

Do not run every test on every viewport.

Choose representative high-risk flows.

---

# 25. Project 1 Step 12 — Execution Report

Create:

```text
docs/07-test-execution-report.md
```

Structure:

```md
# Test Execution Report

## Build / Test Date

## Environment

## Scope

## Summary

| Metric | Result |
|---|---:|
| Total Executed | |
| Passed | |
| Failed | |
| Blocked | |

## Defects

| Severity | Count |
|---|---:|
| Critical | |
| Major | |
| Minor | |
| Suggestion | |

## Critical Findings

## Regression Result

## Automation Result

## Known Limitations

## Release Recommendation
```

Do not fabricate company-style "Go / No-Go" authority.

Phrase it as:

```text
Based on the executed portfolio scope, the tested critical paths are ...
```

---

# 26. Project 1 Definition of Done

Do not proceed to Project 2 until these exist:

- [ ] public demo target selected;
- [ ] 15–25 requirements;
- [ ] exploratory notes;
- [ ] test plan;
- [ ] 30–50 test scenarios;
- [ ] 50–80 detailed test cases;
- [ ] manual execution;
- [ ] at least 3 meaningful real or clearly simulated bug reports;
- [ ] regression scope;
- [ ] Cypress TypeScript project;
- [ ] POM;
- [ ] fixtures;
- [ ] reusable custom command;
- [ ] 15–25 stable automated tests;
- [ ] execution report;
- [ ] project README;
- [ ] no confidential data.

---

# 27. PROJECT 2 — Legacy ERP Migration / System Analysis Case Study

This project demonstrates a different competency.

It is based on the **type of work** you performed when entering an ERP migration project with very limited initial documentation and having to learn the domain and inspect a legacy application.

The public project will recreate this process using a **fictional ERP company and independently created legacy requirements**.

Do not publish actual employer documents.

---

# 28. ERP Public Scenario

Create a fictional company:

```text
PT Demo Manufacturing Indonesia
```

Business:

```text
manufactures metal components
purchases raw materials
produces finished goods
sells to business customers
uses multiple warehouses
```

Legacy system:

```text
old desktop ERP
```

Migration target:

```text
web-based ERP
```

Public case-study problem:

```text
The organization wants to migrate an undocumented legacy desktop ERP to a
modern web application. Formal requirements are incomplete. Existing
application behavior and limited operational references must therefore be
studied to reconstruct the required business functions.
```

---

# 29. ERP Step 1 — Domain Learning Notes

Create:

```text
02-domain-learning-notes.md
```

Document concepts you study:

```text
ERP
Sales
Purchasing
Inventory
Manufacturing
Bill of Materials
Work Order
Purchase Order
Goods Receipt
Sales Order
Delivery
Invoice
Stock movement
Role and permission
Accounting integration
```

Important:

Do not pretend to be an accounting expert.

Label:

```text
Concept understood at system-flow level
```

when appropriate.

---

# 30. ERP Step 2 — Legacy Feature Inventory

Create:

```text
03-legacy-feature-inventory.xlsx
```

Columns:

| Legacy Ref | Area | Legacy Function | Observed Purpose | Inputs | Outputs | Dependencies | Confidence | Open Question |
|---|---|---|---|---|---|---|---|---|

Example:

| Legacy Ref | Area | Legacy Function | Observed Purpose | Inputs | Outputs | Dependencies | Confidence | Open Question |
|---|---|---|---|---|---|---|---|---|
| LEG-PUR-001 | Purchasing | Purchase Order | Create supplier order | supplier, item, qty | PO | supplier master | High | approval required? |
| LEG-INV-003 | Inventory | Stock Correction | Adjust inventory | item, qty, reason | stock movement | warehouse | Medium | who can approve? |

Target:

- 40–80 functions for the portfolio version.

You do not need 165.

---

# 31. ERP Step 3 — Reconstruct Business Flows

Create:

```text
04-business-flow-reconstruction.md
```

Primary flows:

## Purchasing

```text
Purchase Request
→ Purchase Order
→ Goods Receipt
→ Supplier Invoice
→ Inventory Increase
→ Payable
```

## Sales

```text
Customer Order
→ Sales Order
→ Delivery
→ Sales Invoice
→ Inventory Decrease
→ Receivable
```

## Production

```text
Sales Demand / Planning
→ Work Order
→ Raw Material Issue
→ Production
→ Finished Goods Receipt
```

Document for every step:

```text
Actor
Input
Action
Output
Downstream Effect
Open Question
```

---

# 32. ERP Step 4 — Legacy-to-Web Mapping

Create:

```text
05-legacy-to-web-mapping.xlsx
```

Columns:

| Legacy Ref | Legacy Function | Target Module | Target Feature | Mapping Decision | Rationale | Status |
|---|---|---|---|---|---|---|

Mapping values:

```text
RETAIN
ADAPT
MERGE
SPLIT
AUTOMATE
REPORT
CONFIGURATION
REMOVE
TBD
```

Example:

```text
Legacy:
Desktop "User & Password"

Target:
User, Role & Permission

Decision:
ADAPT

Rationale:
Web system requires role-based access and session management.
```

---

# 33. ERP Step 5 — Scope and Open Questions

Create:

```text
06-scope-and-open-questions.xlsx
```

Sheet 1: Scope

| Feature | In Scope | Out of Scope | Phase | Reason |
|---|---|---|---|---|

Sheet 2: Open Questions

| Question ID | Module | Current Understanding | Missing Information | Risk | Proposed Clarification |
|---|---|---|---|---|---|

Example:

```text
OQ-PUR-004
When partially receiving a PO, does the remaining quantity stay open,
auto-close, or require manual closure?
```

This demonstrates that you know:

```text
unknown requirement ≠ assumption
```

---

# 34. ERP Step 6 — Mini SRD

Create:

```text
07-mini-srd.md
```

Recommended structure:

```md
# Software Requirements Document

## 1. Document Information

## 2. Project Background

## 3. Objective

## 4. Scope

## 5. Assumptions

## 6. User Roles

## 7. Module Overview

## 8. Functional Requirements

### 8.1 Purchasing
### 8.2 Sales
### 8.3 Inventory
### 8.4 Manufacturing

## 9. Business Rules

## 10. State Transitions

## 11. Data Requirements

## 12. Non-Functional Requirements

## 13. Open Questions

## 14. Testability Notes
```

Keep the public SRD approximately:

```text
20–35 pages equivalent
```

not 150 pages.

---

# 35. ERP Requirement Format

Use identifiers:

```text
FR-PUR-001
FR-SAL-001
FR-INV-001
FR-MFG-001
```

Example:

```md
### FR-PUR-003 — Purchase Order Submission

Actor:
Purchasing Staff

Preconditions:
- supplier exists;
- at least one item exists.

Main Flow:
1. User creates draft PO.
2. User selects supplier.
3. User adds item and quantity.
4. User submits PO.

Expected State:
PO becomes Submitted.

Validation:
- supplier required;
- quantity > 0;
- item required.
```

---

# 36. ERP State Transition

Example:

```text
DRAFT
↓ submit
SUBMITTED
↓ approve
APPROVED
↓ receive
PARTIALLY RECEIVED
↓ receive remaining
FULLY RECEIVED
↓ close
CLOSED
```

Also test illegal transitions.

Example:

```text
DRAFT → FULLY RECEIVED
```

should be invalid.

---

# 37. ERP Step 7 — Requirement Register

Create:

```text
08-requirement-register.xlsx
```

Columns:

| Requirement ID | Module | Requirement | Source | Priority | Status | Testable | Open Question |
|---|---|---|---|---|---|---|---|

Source can be:

```text
Legacy Observation
Business Assumption
Migration Requirement
Derived Rule
```

Do not label a derived assumption as confirmed business fact.

---

# 38. ERP Step 8 — Traceability Matrix

Create:

```text
09-traceability-matrix.xlsx
```

Columns:

| Requirement ID | Feature | Test Scenario ID | Test Case ID | Status |
|---|---|---|---|---|

Example:

```text
FR-PUR-003
Purchase Order Submission
TS-PUR-007
TC-PUR-021
PASS
```

This shows requirement-to-test traceability.

---

# 39. ERP Step 9 — Selected Test Cases

Create:

```text
10-selected-test-cases.xlsx
```

Do not test the entire ERP.

Select:

```text
Purchasing: 15–20 cases
Sales: 15–20 cases
Inventory: 10–15 cases
Manufacturing: 10–15 cases
Role/Permission: 5–10 cases
```

Target:

```text
60–80 selected system-analysis-derived test cases
```

---

# 40. ERP Definition of Done

- [ ] fictional company defined;
- [ ] domain notes;
- [ ] legacy feature inventory;
- [ ] 3+ reconstructed business flows;
- [ ] legacy-to-web mapping;
- [ ] mapping decision taxonomy;
- [ ] open-question register;
- [ ] mini SRD;
- [ ] requirement register;
- [ ] state transitions;
- [ ] business rules;
- [ ] traceability matrix;
- [ ] selected QA cases;
- [ ] README explains migration analysis;
- [ ] no original internal documents uploaded.

---

# 41. PROJECT 3 — API Testing Case Study

This project exists primarily to demonstrate a competency frequently expected in QA roles.

Target stack:

```text
Postman
REST
JSON
environment variables
positive testing
negative testing
CRUD
assertions
Newman
```

---

# 42. API Step 1 — Choose API

Use:

```text
a public API intended for testing
```

Requirements:

```text
GET
POST
PUT/PATCH
DELETE
authentication if possible
JSON responses
```

---

# 43. API Test Plan

Create:

```text
docs/api-test-plan.md
```

Include:

```text
scope
base URL
authentication
resources
positive paths
negative paths
validation
cleanup strategy
test data
risks
```

---

# 44. API Test Cases

Create:

```text
docs/api-test-cases.xlsx
```

Columns:

| Case ID | Endpoint | Method | Scenario | Headers | Request Body | Expected Status | Expected Validation | Actual | Status |
|---|---|---|---|---|---|---|---|---|---|

Cover:

```text
valid request
missing field
invalid data type
invalid authentication
unknown resource
duplicate request
boundary input
unsupported method
invalid JSON
```

---

# 45. Postman Assertions

Demonstrate:

```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
```

Also:

```text
response property exists
property type
business value
error message
response time
schema
```

---

# 46. Dynamic Data

Example:

```javascript
const id = pm.response.json().id;
pm.environment.set("resource_id", id);
```

Then:

```text
CREATE
→ capture ID
→ READ
→ UPDATE
→ DELETE
```

This is significantly stronger than isolated endpoint calls.

---

# 47. Newman

Run:

```bash
newman run collection.json -e environment.json
```

Optionally install reporter.

Save evidence under:

```text
evidence/reports/
```

---

# 48. API Definition of Done

- [ ] API test plan;
- [ ] 30–50 API cases;
- [ ] Postman collection;
- [ ] environment variables;
- [ ] chained CRUD;
- [ ] positive tests;
- [ ] negative tests;
- [ ] authentication test if available;
- [ ] assertions;
- [ ] Newman execution;
- [ ] report;
- [ ] README.

---

# 49. PROJECT 4 — Selenium Case Study

Optional.

Only build this after Projects 1–3.

Purpose:

```text
show a second automation stack
```

Suggested workflow:

```text
Login
→ upload file
→ processing
→ result
→ download
```

Use a public application or build a tiny demo application yourself.

Do not recreate former employer products.

---

# 50. Git Commit Strategy

Avoid:

```text
final
fix
fix2
latest
test
```

Prefer:

```text
docs: add initial ecommerce requirements
test: add authentication scenarios
test: add cart edge cases
automation: add login page object
automation: add cached authenticated session
docs: add regression strategy
api: add negative authentication tests
erp: add legacy-to-web mapping
```

This itself demonstrates engineering discipline.

---

# 51. GitHub Repository Hygiene

Never commit:

```text
.env
credentials.json
real accounts
screenshots with private information
internal documents
node_modules
reports containing sensitive URLs
```

Example `.gitignore`:

```gitignore
node_modules/
.env
.env.*
!.env.example
cypress/videos/
cypress/downloads/
.DS_Store
Thumbs.db
```

If test credentials are required:

```text
.env.example
```

contains:

```text
TEST_USERNAME=replace_me
TEST_PASSWORD=replace_me
```

not real secrets.

---

# 52. Evidence Folder

Evidence is useful, but do not dump hundreds of screenshots.

Keep:

```text
1 screenshot of report dashboard
1 screenshot of representative passed test
1 screenshot of representative failed test
1 redacted/manual bug screenshot
```

Recruiters need evidence, not noise.

---

# 53. README Template for Every Project

Use:

```md
# Project Title

## 1. Context

## 2. Objective

## 3. System Under Test

## 4. Scope

## 5. QA Approach

## 6. Test Design

## 7. Test Artifacts

## 8. Defects / Findings

## 9. Automation

## 10. Execution Result

## 11. Challenges

## 12. Decisions and Trade-offs

## 13. What I Learned

## 14. Repository Structure

## 15. How to Run

## 16. Confidentiality Notice
```

---

# 54. How to Write "What I Learned"

Bad:

```text
I learned Cypress.
```

Better:

```text
I learned that caching authenticated sessions can significantly reduce
regression execution time, but dedicated authentication tests must still
exercise the full login UI to avoid hiding authentication defects.
```

Another:

```text
I learned that cross-origin payment flows create automation constraints,
so automation scope should be designed around deterministic boundaries
instead of forcing unstable end-to-end assertions.
```

---

# 55. How to Explain the Portfolio in an Interview

For Project 1:

```text
I recreated an independent e-commerce QA case study to demonstrate the
workflow I use professionally: understand requirements, explore the
feature, formalize test coverage, execute manual tests, report defects,
perform regression, then automate stable high-value flows using Cypress
and TypeScript.
```

For Project 2:

```text
I created a legacy ERP migration case study because I have experience
working on a migration project where initial requirements were limited.
The exercise demonstrates how I approach functional discovery: learn the
domain, inspect existing behavior, inventory functions, reconstruct
business flows, identify unknowns, map legacy features to a target web
system, and derive testable requirements.
```

---

# 56. Portfolio Claims: Allowed vs Not Allowed

## Safe

```text
Built an independent Cypress regression portfolio using TypeScript and POM.
Designed test cases covering positive, negative, edge, and state-transition behavior.
Created a legacy ERP requirement-reconstruction case study.
Performed API testing with Postman and chained CRUD validation.
```

## Unsafe unless true

```text
Reduced production defects by 60%.
Built CI/CD pipelines.
Led enterprise ERP architecture.
Performed penetration testing.
Validated financial accounting compliance.
Automated Safari with Cypress.
Tested production systems at scale.
```

---

# 57. Review Workflow With ChatGPT

You should **not** send me the final portfolio only.

Send each artifact incrementally.

Recommended loop:

```text
You build
↓
Send artifact
↓
I review as QA Lead
↓
Score
↓
Corrections
↓
You revise
↓
Next artifact
```

---

# 58. Review Score Rubric

Every artifact can be scored on 100.

## Requirement Understanding — 20

- 0–5 superficial
- 6–10 partially structured
- 11–15 clear and testable
- 16–20 strong requirement reasoning

## Test Design — 25

- coverage
- positive/negative
- edge cases
- appropriate techniques
- risk orientation

## Technical Correctness — 20

- assertions
- selector quality
- state handling
- automation architecture
- test-data handling

## Documentation Quality — 15

- clarity
- reproducibility
- traceability
- professional structure

## Risk / Business Thinking — 10

- critical path
- severity
- regression impact
- open questions

## Maintainability — 10

- reuse
- structure
- naming
- avoiding duplication

Target:

```text
85+ before public release
```

---

# 59. First Execution Sprint

Do not try to finish everything at once.

Your first local sprint is only:

## Sprint 1 — Repository + E-Commerce Discovery

Tasks:

- [ ] Install/verify tools.
- [ ] Create `qa-portfolio`.
- [ ] Initialize Git.
- [ ] Create root README.
- [ ] Create Project 1 folders.
- [ ] Select public e-commerce target.
- [ ] Write 15–25 product requirements.
- [ ] Perform one exploratory session for Login.
- [ ] Perform one exploratory session for Cart.
- [ ] Create first 10 test scenarios.

Stop there.

Do **not** build Cypress yet.

---

# 60. What to Send Me After Sprint 1

Send:

```text
README.md
01-product-requirements.md
05-exploratory-notes.md
03-test-scenarios.xlsx
```

Then ask:

```text
Review Sprint 1 as my QA Lead. Score each artifact, identify weak
reasoning, missing coverage, unsupported assumptions, and what I must fix
before proceeding to detailed test cases.
```

I will then decide whether you are ready for Sprint 2.

---

# 61. Sprint 2

After Sprint 1 passes:

- [ ] create test plan;
- [ ] expand scenarios to 30–50;
- [ ] create 50–80 detailed test cases;
- [ ] mark design techniques;
- [ ] identify automation candidates.

---

# 62. Sprint 3

Manual execution:

- [ ] execute tests;
- [ ] collect evidence;
- [ ] report defects;
- [ ] classify severity;
- [ ] write execution report;
- [ ] define regression scope.

---

# 63. Sprint 4

Cypress:

- [ ] initialize project;
- [ ] TypeScript;
- [ ] POM;
- [ ] fixtures;
- [ ] commands;
- [ ] session;
- [ ] auth suite;
- [ ] search;
- [ ] product;
- [ ] cart;
- [ ] checkout;
- [ ] Mochawesome.

---

# 64. Sprint 5

Portfolio polish:

- [ ] clean README;
- [ ] verify run instructions;
- [ ] remove secrets;
- [ ] verify repository from fresh clone;
- [ ] add representative evidence;
- [ ] final review;
- [ ] push public.

---

# 65. ERP Execution Sprints

Only after Project 1 is solid.

## ERP Sprint 1
- fictional company;
- domain notes;
- legacy feature inventory.

## ERP Sprint 2
- flow reconstruction;
- feature dependencies;
- open questions.

## ERP Sprint 3
- legacy-to-web mapping;
- scope classification;
- requirements.

## ERP Sprint 4
- mini SRD;
- state transitions;
- business rules.

## ERP Sprint 5
- traceability;
- selected QA test cases;
- README.

---

# 66. API Execution Sprints

## API Sprint 1
- API selection;
- Postman basics;
- test plan.

## API Sprint 2
- CRUD;
- variables;
- assertions.

## API Sprint 3
- negative testing;
- chained flows;
- Newman.

## API Sprint 4
- README;
- evidence;
- final review.

---

# 67. Expected Final Recruiter Experience

When a recruiter opens your GitHub, they should understand your profile in under 2 minutes:

```text
This person can manually test.
This person understands test design.
This person can report defects.
This person can automate.
This person understands regression.
This person can debug web behavior.
This person knows basic API testing.
This person can reason from requirements.
This person has exposure to complex ERP/system-analysis work.
```

That is the objective.

Not:

```text
This person uploaded 25 random Excel files.
```

---

# 68. Final Rule

Do not optimize for:

```text
number of test cases
number of repositories
number of tools
number of screenshots
```

Optimize for:

```text
quality of reasoning
traceability
risk awareness
technical correctness
reproducibility
clarity
evidence of ownership
```

One strong case study is worth more than five shallow repositories.

---

# 69. Your Immediate Next Action

Execute only this:

```text
1. Create the local qa-portfolio repository.
2. Create the root README.
3. Create Project 1 folder structure.
4. Select the public e-commerce target.
5. Write the initial product requirements.
6. Perform exploratory sessions for Login and Cart.
7. Write the first 10 test scenarios.
8. Send those artifacts for review.
```

Do not start Cypress before this checkpoint.

That is **Sprint 1**.

---

# 70. GitHub Publication Checkpoint

Before asking for a repository audit, verify:

```text
Repository is accessible through the link you will send.
README renders correctly.
Important XLSX/PDF artifacts are present and named clearly.
Automation source is visible.
No generated noise dominates the repository.
No secrets or internal company material are present.
Latest local commits are pushed.
```

Run:

```bash
git status
git log --oneline -10
git remote -v
git push
```

Expected `git status` before review:

```text
nothing to commit, working tree clean
```

---

# 71. Recommended Repository Review Requests

## Sprint Review

```text
Review the latest Sprint of my QA portfolio from this GitHub repository.
Score only the artifacts required for this sprint. Identify missing
coverage, unsupported assumptions, weak QA reasoning, and mandatory fixes.
Do not let me proceed to the next sprint unless the current sprint is ready.
```

## Automation Audit

```text
Audit the Cypress project itself. Inspect specs, Page Objects, fixtures,
custom commands, session handling, assertions, selectors, duplication,
flakiness risk, and test isolation. Do not judge only from the README.
```

## Final Recruiter Audit

```text
Audit this repository as both a QA Lead and a recruiter screening a junior
QA candidate. First judge technical QA quality, then tell me what a
recruiter can understand in the first two minutes, what creates doubt, and
what should be improved before I put this GitHub link on my CV.
```

---

# 72. Final Build-from-Zero Workflow

The complete workflow is now:

```text
0. Install tooling
1. Create local workspace
2. Initialize Git
3. Configure .gitignore
4. Create GitHub repository
5. Connect origin
6. Push initial structure
7. Build Sprint 1 locally
8. Review staged changes
9. Commit meaningful changes
10. Push to GitHub
11. Send public link for QA Lead review
12. Fix locally
13. Commit + push revision
14. Continue to next sprint
15. Fresh-clone validation
16. Security/confidentiality review
17. Final recruiter audit
18. Put GitHub portfolio link on tailored CV
```

This is the operating model for the portfolio project.

