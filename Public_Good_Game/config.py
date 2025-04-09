
from string import Template

class Config:

    def __init__(self, header, steps):
        self.instruction = self.get_Instruction( header, steps)

    def get_Instruction(self, header, steps) : 
        return f"""
        <div class="card-body lh-lg  ">
            <p> {header}</p>
            <ol>
                {"".join([f"<li>{step}</li>" for step in steps])}
            </ol>
        </div>
"""
    
    def format_string(self, probability, cost, endowment):
        template = Template(self.instruction)
        self.instruction  = template.substitute(probability=probability, cost=cost, endowment=endowment)