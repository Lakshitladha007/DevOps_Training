Merge Conflict Resolution

Depending on our workflow there are various ways for conflict resolution.

1. For small conflicts: Manual resolution
   
Open the conflicted file/files and look for conflict markers (<<<<<<<, =======, 
>>>>>>>). Now here decide which changes to keep or merge and remove the 
conflict markers and save the file. Add and merge the resolved file.
>>>>>>>
2. For GUI users: VS Code or Sourcetree
   
Git tools provide an interactive way to resolve conflicts. VS Code shows conflict 
markers with “Accept Incoming”, “Accept Current” or “Accept Both”. Sourcetree 
offers a UI to resolve conflicts easily.

3. For structured history: Rebase the code instead of merge
   
Instead of merging, we can rebase to keep a cleaner history. Rebase moves our 
branch’s changes on top of another branch instead of merging them. 
It is not advised to use rebase on public/shared branches and when merge history is 
required by the team. It is also not preferrable when merging large and long-lived 
brancches. 
Command for Basic Rebase: git rebase main
