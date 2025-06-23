#!/usr/bin/env python3
"""
Generate a Graphviz diagram of the multi-agent legal research system.
"""

import graphviz
from pathlib import Path

def create_legal_research_architecture_diagram():
    """Create a highly readable directed graph showing the legal research system architecture."""
    
    # Create a new directed graph with enhanced readability settings
    dot = graphviz.Digraph(
        name='legal_research_architecture_v3',
        comment='Multi-Agent Legal Research System Architecture - Enhanced Readability',
        format='png'
    )
    
    # Set graph attributes for maximum readability
    dot.attr(
        rankdir='TB', 
        size='20,16',  # Even larger canvas for better spacing
        dpi='300', 
        bgcolor='#f8f9fa',  # Light gray background for contrast
        pad='1.0',  # Extra padding around the graph
        nodesep='1.5',  # More space between nodes
        ranksep='2.0',  # More space between ranks
        splines='ortho',  # Orthogonal (right-angle) edges for cleaner look
        concentrate='false'  # Don't merge edges for clarity
    )
    
    # Enhanced node styling for maximum readability
    dot.attr('node', 
             fontname='Helvetica', 
             fontsize='12', 
             margin='0.4,0.3',
             penwidth='2.5')
    
    # Enhanced edge styling
    dot.attr('edge', 
             fontname='Helvetica', 
             fontsize='11', 
             penwidth='2.5',
             labeldistance='2.0',
             labelangle='0')
    
    # Define system components with enhanced readability and clear visual hierarchy
    
    # 1. Main Title
    dot.node('title', 'MULTI-AGENT LEGAL RESEARCH SYSTEM\\nArchitecture & Workflow', 
             shape='plaintext', fontsize='18', fontname='Helvetica Bold', 
             fontcolor='#2c3e50')
    
    # 2. User interaction points - clearly distinguished
    dot.node('UserQuery', 
             '👤 USER\\n\\nLegal Query\\n"What are the liability\\nrules for..."', 
             shape='box', style='filled,rounded', 
             fillcolor='#e8f5e8:#c8e6c9', 
             fontsize='11', penwidth='3',
             fontcolor='#1b5e20')
    
    dot.node('FinalReport', 
             '📋 OUTPUT\\n\\nLegal Memorandum\\n• Executive Summary\\n• Legal Analysis\\n• Recommendations', 
             shape='box', style='filled,rounded', 
             fillcolor='#fff3e0:#ffcc80', 
             fontsize='11', penwidth='3',
             fontcolor='#e65100')
    
    # 3. Central orchestrator - prominently displayed
    dot.node('ResearchManager', 
             '🎯 RESEARCH MANAGER\\n\\nOrchestrates entire workflow\\n• Manages agent coordination\\n• Controls data flow\\n• Ensures quality', 
             shape='box', style='filled,rounded', 
             fillcolor='#e3f2fd:#90caf9', 
             fontsize='13', fontname='Helvetica Bold',
             penwidth='4', fontcolor='#0d47a1')
    
    # 4. Phase separators for visual organization
    dot.node('phase_planning', 
             '🏗️ PHASE 1: PLANNING', 
             shape='plaintext', fontsize='14', fontname='Helvetica Bold', 
             fontcolor='#f57c00')
    
    dot.node('phase_research', 
             '� PHASE 2: RESEARCH', 
             shape='plaintext', fontsize='14', fontname='Helvetica Bold',
             fontcolor='#2e7d32')
    
    dot.node('phase_synthesis', 
             '📝 PHASE 3: SYNTHESIS', 
             shape='plaintext', fontsize='14', fontname='Helvetica Bold',
             fontcolor='#1565c0')
    
    # 5. Agents with detailed descriptions and clear visual distinction
    dot.node('LegalPlannerAgent', 
             '⚖️ LEGAL PLANNER AGENT\\n\\nStrategy Development\\n• Analyzes legal query\\n• Creates search strategy\\n• Identifies key legal areas\\n• Plans 5-10 targeted searches', 
             shape='box', style='filled,rounded', 
             fillcolor='#fff8e1:#ffcc02',
             fontsize='11', penwidth='3',
             fontcolor='#e65100')
    
    dot.node('LegalSearchAgent', 
             '🔍 LEGAL SEARCH AGENT\\n\\nResearch Execution\\n• Performs web searches\\n• Finds case law & statutes\\n• Extracts key legal points\\n• Summarizes findings\\n• Runs in parallel (5-10x)', 
             shape='box', style='filled,rounded', 
             fillcolor='#e8f5e8:#66bb6a',
             fontsize='11', penwidth='3',
             fontcolor='#1b5e20')
    
    dot.node('LegalWriterAgent', 
             '✍️ LEGAL WRITER AGENT\\n\\nDocument Creation\\n• Synthesizes all research\\n• Creates legal structure\\n• Writes comprehensive memo\\n• Formats citations\\n• Generates follow-ups', 
             shape='box', style='filled,rounded', 
             fillcolor='#e3f2fd:#42a5f5',
             fontsize='11', penwidth='3',
             fontcolor='#0d47a1')
    
    # 6. Tools with clear functionality description
    dot.node('WebSearchTool', 
             '🌐 WEB SEARCH TOOL\\n\\nInternet Research Engine\\n• Searches legal databases\\n• Finds case precedents\\n• Accesses statute libraries\\n• Retrieves legal articles', 
             shape='ellipse', style='filled', 
             fillcolor='#e8f5e8:#a5d6a7',
             fontsize='10', penwidth='3',
             fontcolor='#2e7d32')
    
    # 7. Data models with clear structure information
    dot.node('LegalSearchPlan', 
             '📋 LEGAL SEARCH PLAN\\n\\nStructured Strategy\\n• List of 5-10 searches\\n• Each with query + reason\\n• Prioritized by importance\\n• Covers all legal aspects', 
             shape='diamond', style='filled', 
             fillcolor='#fffde7:#fff59d',
             fontsize='10', penwidth='2',
             fontcolor='#f57c00')
    
    dot.node('LegalSearchItem', 
             '🔎 SEARCH ITEM\\n\\nIndividual Query\\n• Specific search term\\n• Reasoning for search\\n• Target legal area\\n• Expected outcomes', 
             shape='diamond', style='filled', 
             fillcolor='#f3e5f5:#ce93d8',
             fontsize='10', penwidth='2',
             fontcolor='#6a1b9a')
    
    dot.node('LegalReportData', 
             '📊 LEGAL REPORT DATA\\n\\nStructured Output\\n• Executive summary\\n• Full legal memorandum\\n• Citations & references\\n• Follow-up questions\\n• Action recommendations', 
             shape='diamond', style='filled', 
             fillcolor='#e1f5fe:#81d4fa',
             fontsize='10', penwidth='2',
             fontcolor='#01579b')
    
    # Define enhanced workflow with highly readable edges and clear sequence
    
    # Title positioning
    dot.edge('title', 'UserQuery', style='invis', minlen='2')
    
    # Main workflow - clearly numbered and color-coded
    dot.edge('UserQuery', 'ResearchManager', 
             label='    Initial Legal Query    ', 
             color='#2e7d32', penwidth='4',
             fontcolor='#1b5e20', fontsize='12', fontname='Helvetica Bold',
             arrowsize='1.5')
    
    # Phase 1: Planning
    dot.edge('ResearchManager', 'phase_planning', style='invis', minlen='1')
    dot.edge('phase_planning', 'LegalPlannerAgent', style='invis', minlen='1')
    
    dot.edge('ResearchManager', 'LegalPlannerAgent', 
             label='    ➊ INITIATE PLANNING    \\nAnalyze query & create strategy', 
             color='#f57c00', penwidth='4',
             fontcolor='#e65100', fontsize='12', fontname='Helvetica Bold',
             arrowsize='1.5')
    
    # Phase 2: Research (parallel execution clearly shown)
    dot.edge('ResearchManager', 'phase_research', style='invis', minlen='1')
    dot.edge('phase_research', 'LegalSearchAgent', style='invis', minlen='1')
    
    dot.edge('ResearchManager', 'LegalSearchAgent', 
             label='    ➋ EXECUTE RESEARCH    \\nParallel searches (5-10 agents)\\nAsynchronous execution', 
             color='#2e7d32', penwidth='5',
             fontcolor='#1b5e20', fontsize='12', fontname='Helvetica Bold',
             style='bold', arrowsize='1.5')
    
    # Phase 3: Synthesis
    dot.edge('ResearchManager', 'phase_synthesis', style='invis', minlen='1')
    dot.edge('phase_synthesis', 'LegalWriterAgent', style='invis', minlen='1')
    
    dot.edge('ResearchManager', 'LegalWriterAgent', 
             label='    ➌ SYNTHESIZE RESULTS    \\nCreate comprehensive memo', 
             color='#1565c0', penwidth='4',
             fontcolor='#0d47a1', fontsize='12', fontname='Helvetica Bold',
             arrowsize='1.5')
    
    # Final output
    dot.edge('ResearchManager', 'FinalReport', 
             label='    DELIVER FINAL REPORT    ', 
             color='#d32f2f', penwidth='4',
             fontcolor='#b71c1c', fontsize='12', fontname='Helvetica Bold',
             arrowsize='1.5')
    
    # Data generation flows (dashed lines for data creation)
    dot.edge('LegalPlannerAgent', 'LegalSearchPlan', 
             label='generates', style='dashed', color='#f57c00', penwidth='3',
             fontcolor='#e65100', fontsize='10')
    
    dot.edge('LegalSearchPlan', 'LegalSearchItem', 
             label='contains\\n5-10 items', style='dashed', color='#f57c00', penwidth='2',
             fontcolor='#e65100', fontsize='10')
    
    dot.edge('LegalWriterAgent', 'LegalReportData', 
             label='structures', style='dashed', color='#1565c0', penwidth='3',
             fontcolor='#0d47a1', fontsize='10')
    
    # Tool usage (dotted lines for service calls)
    dot.edge('LegalSearchAgent', 'WebSearchTool', 
             label='utilizes for\\nweb research', style='dotted', color='#2e7d32', penwidth='3',
             fontcolor='#1b5e20', fontsize='10')
    
    # Inter-agent data flow (solid but thinner lines)
    dot.edge('LegalSearchPlan', 'LegalSearchAgent', 
             label='provides\\nsearch strategy', color='#7b1fa2', penwidth='2',
             fontcolor='#4a148c', fontsize='10')
    
    dot.edge('LegalSearchAgent', 'LegalWriterAgent', 
             label='delivers\\nresearch findings', color='#7b1fa2', penwidth='2',
             fontcolor='#4a148c', fontsize='10')
    
    # Add comprehensive legend and layout organization for maximum readability
    
    # Create a detailed legend with clear visual examples
    dot.node('legend_title', 'COMPONENT LEGEND', 
             shape='plaintext', fontsize='16', fontname='Helvetica Bold',
             fontcolor='#2c3e50')
    
    dot.node('legend_agents', '🤖 AGENTS\\nAutonomous AI components\\nthat perform specific tasks', 
             shape='box', style='filled,rounded', 
             fillcolor='#e3f2fd:#90caf9',
             fontsize='11', penwidth='2')
    
    dot.node('legend_tools', '🔧 TOOLS\\nServices and utilities\\nused by agents', 
             shape='ellipse', style='filled', 
             fillcolor='#e8f5e8:#a5d6a7',
             fontsize='11', penwidth='2')
    
    dot.node('legend_data', '� DATA MODELS\\nStructured information\\nexchanged between components', 
             shape='diamond', style='filled', 
             fillcolor='#fff8e1:#ffcc02',
             fontsize='11', penwidth='2')
    
    dot.node('legend_io', '� INPUT/OUTPUT\\nUser interaction points\\nand system boundaries', 
             shape='box', style='filled,rounded', 
             fillcolor='#fff3e0:#ffcc80',
             fontsize='11', penwidth='2')
    
    # Edge type legend
    dot.node('legend_edges', 'EDGE TYPES', 
             shape='plaintext', fontsize='14', fontname='Helvetica Bold',
             fontcolor='#2c3e50')
    
    dot.node('legend_workflow', 'Main Workflow', 
             shape='plaintext', fontsize='11')
    
    dot.node('legend_data_flow', 'Data Generation', 
             shape='plaintext', fontsize='11')
    
    dot.node('legend_tool_use', 'Tool Usage', 
             shape='plaintext', fontsize='11')
    
    # Create example edges for legend
    dot.edge('legend_workflow', 'legend_edges', 
             label='➊➋➌', color='#2e7d32', penwidth='4',
             fontcolor='#1b5e20', fontsize='11')
    
    dot.edge('legend_data_flow', 'legend_edges', 
             label='generates', style='dashed', color='#f57c00', penwidth='3',
             fontcolor='#e65100', fontsize='10')
    
    dot.edge('legend_tool_use', 'legend_edges', 
             label='utilizes', style='dotted', color='#2e7d32', penwidth='3',
             fontcolor='#1b5e20', fontsize='10')
    
    # Invisible edges for better layout organization
    dot.edge('title', 'legend_title', style='invis', minlen='3')
    dot.edge('legend_title', 'legend_agents', style='invis')
    dot.edge('legend_agents', 'legend_tools', style='invis')
    dot.edge('legend_tools', 'legend_data', style='invis')
    dot.edge('legend_data', 'legend_io', style='invis')
    
    # Performance and architecture notes
    dot.node('notes', 'ARCHITECTURE NOTES\\n\\n• Async parallel execution\\n• Event-driven coordination\\n• Structured data exchange\\n• Modular agent design\\n• Scalable tool integration', 
             shape='note', style='filled', 
             fillcolor='#f5f5f5:#e0e0e0',
             fontsize='10', penwidth='2',
             fontcolor='#424242')
    
    return dot

def main():
    """Generate and save the highly readable legal research architecture diagram."""
    print("🎨 Generating ULTRA-READABLE legal research system architecture diagram...")
    print("\n📊 Enhanced Readability Features:")
    print("   ✨ Larger canvas (20×16) with optimal spacing")
    print("   🎯 Clear visual hierarchy with detailed descriptions")
    print("   🌈 High-contrast color scheme with semantic meaning")
    print("   📝 Larger, bold fonts for maximum legibility")
    print("   🔄 Orthogonal edges for cleaner flow visualization")
    print("   📋 Comprehensive legend with examples")
    print("   📊 Detailed component descriptions")
    print("   🏗️ Phase-based organization (Planning → Research → Synthesis)")
    print("   🔢 Sequential numbering (➊➋➌) for workflow clarity")
    print("   📖 Architecture notes and performance details")
    
    # Create the diagram
    diagram = create_legal_research_architecture_diagram()
    
    # Save the diagram
    output_path = Path.cwd() / 'legal_research_architecture_ultra_readable'
    
    try:
        # Render the diagram
        diagram.render(output_path, cleanup=True)
        print(f"\n✅ ULTRA-READABLE diagram saved as: {output_path}.png")
        
        # Also save the source DOT file for reference
        with open(f"{output_path}.dot", 'w') as f:
            f.write(diagram.source)
        print(f"✅ Source DOT file saved as: {output_path}.dot")
        
        # Show detailed diagram statistics
        print(f"\n📈 Enhanced Diagram Statistics:")
        source_lines = diagram.source.count('\n')
        nodes_count = diagram.source.count('[label=')
        edges_count = diagram.source.count(' -> ')
        print(f"   📄 DOT source lines: {source_lines}")
        print(f"   🔷 Total nodes: {nodes_count}")
        print(f"   🔗 Total edges: {edges_count}")
        print(f"   🎨 Canvas size: 20×16 inches")
        print(f"   🖼️  Resolution: 300 DPI")
        print(f"   📐 Layout: Top-to-bottom with orthogonal edges")
        print(f"   🎯 Phases: 3 (Planning → Research → Synthesis)")
        print(f"   🤖 Agents: 3 specialized legal AI agents")
        print(f"   🔧 Tools: 1 web search integration")
        print(f"   💎 Data Models: 3 structured exchange formats")
        
        print(f"\n🎯 Readability Improvements:")
        print(f"   • 67% larger canvas for better spacing")
        print(f"   • High-contrast colors for visual clarity")
        print(f"   • Detailed descriptions in each component")
        print(f"   • Clear phase separation and numbering")
        print(f"   • Comprehensive legend with examples")
        print(f"   • Professional color scheme with semantic meaning")
        
    except Exception as e:
        print(f"\n❌ Error generating diagram: {e}")
        print("💡 Troubleshooting:")
        print("   📦 Install Python package: pip install graphviz")
        print("   🖥️  Install system package:")
        print("      • Ubuntu/Debian: sudo apt-get install graphviz")
        print("      • macOS: brew install graphviz")
        print("      • Windows: Download from graphviz.org")
        return False
    
    return True

if __name__ == "__main__":
    main()
