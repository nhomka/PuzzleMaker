class CellValue:
    value = 0
    rules = {}
    
    def __init__(self, cell_text):
        self.value = int(cell_text[-1])
        self.rules = {}
        self.parse_rules(cell_text)
        
    def parse_rules(self, rules):
        for rule in rules.split(';')[:-1]:
            rule_name, rule_value = rule.split(':')
            rule_id, rule_value = rule_value.split('-')
            self.rules[rule_name] = (rule_id, rule_value)
            
    def __str__(self):
        return(self.value)