import functools

# Decorator
def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"
    return wrapper

class Report:
    templates = {}

    def __init__(self, title):
        self.title = title
        self.sections = []

    @classmethod
    def register_template(cls, name, sections):
        cls.templates[name] = sections

    @classmethod
    def from_template(cls, name, title):
        report = cls(title)
        report.sections = cls.templates.get(name, [])
        return report

    @bold
    def show_title(self):
        return self.title

    # Magic Methods
    def __len__(self):
        return len(self.sections)

    def __getitem__(self, index):
        return self.sections[index]

    def __contains__(self, item):
        return item in self.sections

    def __str__(self):
        return f"Report: {self.title}\nSections: {self.sections}"

# Driver Code
Report.register_template(
    "project",
    ["Introduction", "Methodology", "Results", "Conclusion"]
)

r = Report.from_template("project", "AI Lab Project")

print(r.show_title())
print("Total Sections:", len(r))
print("First Section:", r[0])
print("Results" in r)
print(r)