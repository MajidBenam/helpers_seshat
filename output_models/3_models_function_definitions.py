########## Beginning of Function Definitions for CrisisDB Models

def call_my_name(self):
    if self.year_from == self.year_to or ((not self.year_to) and self.year_from):
        return self.name + " [for " + self.polity.name + " in " + str(self.year_from) + "]"
    else:
        return self.name + " [for " + self.polity.name + " from " + str(self.year_from) + " to " + str(self.year_to) + "]"


def return_citations(self):
    return ', '.join(['<a href="' + citation.zoteroer() + '">' + citation.__str__() + ' </a>' for citation in self.citations.all()[:2]])


def clean_times(self):
    if (self.year_from and self.year_to) and self.year_from > self.year_to:
        raise ValidationError({
            'year_from': 'The start year is bigger than the end year!',
        })
    if self.year_from and (self.year_from < -10000 or self.year_from > date.today().year):
        raise ValidationError({
            'year_from': 'The start year is out of range!',
        })
    if self.year_from and (self.year_from < self.polity.start):
        raise ValidationError({
            'year_from': 'The start year is earlier than the start year of the corresponding polity!',
        })
    if self.year_to and (self.year_to > self.polity.end):
        raise ValidationError({
            'year_to': 'The end year is later than the end year of the corresponding polity!',
        })
    if self.year_to and (self.year_to < -10000 or self.year_to > date.today().year):
        raise ValidationError({
            'year_to': 'The end year is out of range!',
        })
    if not self.year_to and not self.year_from:
        raise ValidationError({
            'year_from': 'You need to enter at least one year (From or To)',
        })

########## End of Function Definitions for CrisisDB Models
