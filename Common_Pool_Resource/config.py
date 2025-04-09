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
    
    def format_string(self, endowment, cost, probability):
        template = Template(self.instruction)
        self.instruction  = template.substitute(endowment=endowment, cost=cost, probability=probability)