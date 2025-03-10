GIT workflow strategies

1. Centralized Workflow: If we consider a small web development agency with 3-4 
developers working on client’s website. They all can directly push changes and 
manually resolve conflicts when needed. 
This type of workflow is centralized workflow and is most beneficial for small teams,
legacy systems and solo developers. Developers can clone the repository, make 
changes, and push directly to the main branch.

2. Feature Branch Workflow: Consider a fintech company developing a mobile app 
for banking, here the developers are creating separate branches for login, payment, 
bank statement, etc. Once a feature is complete and tested, then it is merged into 
the main branch. 
This type of workflow is suitable for parallel development and agile teams (where 
new features are required to be frequently released). This is used with startups and 
mid-sized companies. Here the main branch remains stable.

3. Git Flow: A gaming company working on some game and developers create a 
feature/* branches for new game mechanics. Once features are merged into 
develop, a release/* branch is created. When the game update is ready, release/* is 
merged into main, and a version (v1.0) is tagged.
This type of workflow is git flow and is useful for Cloud and SaaS applications. It’s 
use case lies with large teams where there is structured release management.

4. GitHub Flow: GitHub-Flow simplifies Git-Flow by eliminating release branches. It
revolves around one active development branch (often main or master) that is directly
deployed to production. Features and bug fixes are implemented using long-living feature
branches. Feedback loops and asynchronous collaboration, common in open-source projects,
are encouraged.

5. Trunk-Based Development: Chrome’s team releases frequent browser updates 
and engineers directly commit to the main branch with feature flags and continuous 
testing. New versions are released every 4-8 weeks.
This type of workflow is trunk-based development and encourages small, frequent 
commits to avoid merging conflicts. This is best for teams practicing continuous 
integration (CI) and continuous deployment (CD). It is popular with fast 
development and high-performance teams.
