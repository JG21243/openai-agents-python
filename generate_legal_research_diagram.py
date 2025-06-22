#!/usr/bin/env python3
"""
Generate a Graphviz diagram of the multi-agent legal research system.
"""

import graphviz
from pathlib import Path

def create_legal_research_architecture_diagram():
    """Create a directed graph showing the legal research system architecture."""
    
    # Create a new directed graph
    dot = graphviz.Digraph(
        name='legal_research_architecture',
        comment='Multi-Agent Legal Research System Architecture',
        format='png'
    )
    
    # Set graph attributes for better layout
    dot.attr(rankdir='TB', size='12,8', dpi='300')
    dot.attr('node', fontname='Arial', fontsize='10')
    dot.attr('edge', fontname='Arial', fontsize='8')
    
    # Define the main system components
    
    # 1. Entry point / Manager
    dot.node('ResearchManager', 'ResearchManager\n(Orchestrator)', 
             shape='box', style='filled', fillcolor='lightblue', fontsize='12')
    
    # 2. Agents (yellow boxes)
    dot.node('LegalPlannerAgent', 'LegalPlannerAgent\n(Planning Phase)', 
             shape='box', style='filled', fillcolor='yellow')
    
    dot.node('LegalSearchAgent', 'LegalSearchAgent\n(Research Phase)', 
             shape='box', style='filled', fillcolor='yellow')
    
    dot.node('LegalWriterAgent', 'LegalWriterAgent\n(Synthesis Phase)', 
             shape='box', style='filled', fillcolor='yellow')
    
    # 3. Tools (green ellipses)
    dot.node('WebSearchTool', 'WebSearchTool\n(Web Search)', 
             shape='ellipse', style='filled', fillcolor='lightgreen')
    
    # 4. Data Models / Output Types (purple diamonds)
    dot.node('LegalSearchPlan', 'LegalSearchPlan\n(Search Strategy)', 
             shape='diamond', style='filled', fillcolor='lavender')
    
    dot.node('LegalSearchItem', 'LegalSearchItem\n(Individual Search)', 
             shape='diamond', style='filled', fillcolor='lavender')
    
    dot.node('LegalReportData', 'LegalReportData\n(Final Report)', 
             shape='diamond', style='filled', fillcolor='lavender')
    
    # 5. External components
    dot.node('UserQuery', 'User Legal Query\n(Input)', 
             shape='box', style='filled', fillcolor='lightyellow')
    
    dot.node('FinalReport', 'Legal Memorandum\n(Output)', 
             shape='box', style='filled', fillcolor='lightcoral')
    
    # Define the workflow edges (solid arrows for agent-to-agent flow)
    
    # Main workflow
    dot.edge('UserQuery', 'ResearchManager', label='legal query')
    dot.edge('ResearchManager', 'LegalPlannerAgent', label='1. plan_searches()')
    dot.edge('ResearchManager', 'LegalSearchAgent', label='2. perform_searches()\n(parallel)', style='bold')
    dot.edge('ResearchManager', 'LegalWriterAgent', label='3. write_report()')
    dot.edge('ResearchManager', 'FinalReport', label='final output')
    
    # Agent outputs
    dot.edge('LegalPlannerAgent', 'LegalSearchPlan', label='produces', style='dashed', color='blue')
    dot.edge('LegalSearchPlan', 'LegalSearchItem', label='contains', style='dashed', color='blue')
    dot.edge('LegalWriterAgent', 'LegalReportData', label='produces', style='dashed', color='blue')
    
    # Tool usage (dotted edges)
    dot.edge('LegalSearchAgent', 'WebSearchTool', label='uses', style='dotted', color='green')
    
    # Data flow between agents
    dot.edge('LegalSearchPlan', 'LegalSearchAgent', label='search plan', style='dashed', color='purple')
    dot.edge('LegalSearchAgent', 'LegalWriterAgent', label='search results', style='dashed', color='purple')
    
    # Add a legend
    with dot.subgraph(name='cluster_legend') as legend:
        legend.attr(label='Legend', fontsize='14', style='filled', fillcolor='white')
        legend.node('legend_agent', 'Agent', shape='box', style='filled', fillcolor='yellow')
        legend.node('legend_tool', 'Tool', shape='ellipse', style='filled', fillcolor='lightgreen')
        legend.node('legend_data', 'Data Model', shape='diamond', style='filled', fillcolor='lavender')
        legend.node('legend_io', 'Input/Output', shape='box', style='filled', fillcolor='lightyellow')
        
        # Legend edges (invisible to just show the types)
        legend.edge('legend_agent', 'legend_tool', label='Tool Usage', style='dotted', color='green')
        legend.edge('legend_agent', 'legend_data', label='Data Flow', style='dashed', color='blue')
    
    # Add subgraphs for logical grouping
    with dot.subgraph(name='cluster_planning') as planning:
        planning.attr(label='Planning Phase', style='filled', fillcolor='lightyellow', alpha='0.3')
        planning.node('LegalPlannerAgent')
        planning.node('LegalSearchPlan')
        planning.node('LegalSearchItem')
    
    with dot.subgraph(name='cluster_research') as research:
        research.attr(label='Research Phase', style='filled', fillcolor='lightcyan', alpha='0.3')
        research.node('LegalSearchAgent')
        research.node('WebSearchTool')
    
    with dot.subgraph(name='cluster_synthesis') as synthesis:
        synthesis.attr(label='Synthesis Phase', style='filled', fillcolor='mistyrose', alpha='0.3')
        synthesis.node('LegalWriterAgent')
        synthesis.node('LegalReportData')
    
    return dot

def main():
    """Generate and save the legal research architecture diagram."""
    print("Generating legal research system architecture diagram...")
    
    # Create the diagram
    diagram = create_legal_research_architecture_diagram()
    
    # Save the diagram
    output_path = Path.cwd() / 'legal_research_architecture'
    
    try:
        # Render the diagram
        diagram.render(output_path, cleanup=True)
        print(f"✅ Diagram saved as: {output_path}.png")
        
        # Also save the source DOT file for reference
        with open(f"{output_path}.dot", 'w') as f:
            f.write(diagram.source)
        print(f"✅ Source DOT file saved as: {output_path}.dot")
        
    except Exception as e:
        print(f"❌ Error generating diagram: {e}")
        print("Make sure Graphviz is installed: pip install graphviz")
        print("And the Graphviz system package: sudo apt-get install graphviz (Ubuntu/Debian)")
        return False
    
    return True

if __name__ == "__main__":
    main()
