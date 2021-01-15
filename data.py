import time

class Project():
    #project data with name and links
    def __init__(self, name, links):
        self.name = name
        self.links = links
    def get_name(self):
        return self.name
    def get_links(self):
        return self.links

class Projects():
    #HTML data with source and projects
    def __init__(self, source, projects):
        self.source = source
        self.projects = projects
    #source data getter
    def get_source(self):
        return self.source
    #project data getter
    def get_projects(self):
        return self.projects

class Link():
    #link data with button and href (url)
    def __init__(self, btn, href):
        self.btn = btn
        self.href = href
    def get_btn(self):
        return self.btn
    def get_href(self):
        return self.href


def setup():
    #Source Data
    name = "Ducks"
    github = "https://github.com/LordRoop/P4-Ducks/blob/main/README.md"
    youtube = "https://www.youtube.com/channel/UClIKOsDS5dsfzFA3zveDT3Q?view_as=subscriber"
    source = {"name": name, "github": github, "youtube": youtube}
    #Project Data
    project1 =  "Tic Tac Toe"
    projlinks1 = [
        Link("Project Plan", "https://docs.google.com/document/d/1TrdnML3xLl7O9xngmHF_PhhplpftU3AHa3l-TyHoe8g"),
        Link("Repl", "https://repl.it/@JSinghSD/CS-P-Tic-Tac-Toe-Groop#README.md")
    ]
    project2 =  "Flask Project"
    projlinks2 = [
        Link("Project Plan", "https://docs.google.com/document/d/16C-jplZo7MnuTXzWabPOHMUYzwajv9OjvTR47Zf347o"),
        Link("Github", "https://github.com/LordRoop/P4-Ducks")
    ]
    #Project Objects
    proj1 = Project(project1, projlinks1)
    proj2 = Project(project2, projlinks2)
    #HTML Data
    projects = Projects(source, [proj1, proj2])
    return projects

def runtime():
    greeting = "(Teacher Rating And Evaluation)"
    doa = time.strftime("%Y-%m-%d %H:%M", time.localtime())
    doah = int(time.strftime("%H", time.localtime()))
    job = "Runtime Link"
    embed = "https://Python-Web-Portfolio-Series.jmort1021.repl.co"
    info = {"greeting": greeting, "doa": doa, "doah": doah, "job": job, "embed": embed}
    return info
