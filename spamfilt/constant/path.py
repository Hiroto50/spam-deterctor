import git 
rep = git.Repo('.', search_parent_directories=True)
ROOT_PATH = rep.working_tree_dir.replace("\\",'/') + "/spam-deterctor"