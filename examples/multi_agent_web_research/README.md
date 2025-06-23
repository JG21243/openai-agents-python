# Multi-Agent Legal Research System

This is a complete multi-agent legal research system designed to assist with legal queries, case law research, and legal document preparation. To run it:

```bash
python -m examples.multi_agent_web_research.main
```

## Legal Agents in the System

### 1. LegalPlannerAgent (`planner_agent.py`)
- **Purpose**: Creates strategic research plans for legal queries
- **Function**: Takes a legal question and generates 5-10 targeted web searches
- **Output**: Structured plan with search terms and reasoning focused on finding case law, statutes, and legal precedents
- **Model**: Uses `o4-mini` for efficient planning

### 2. LegalSearchAgent (`search_agent.py`)
- **Purpose**: Performs specialized web searches for legal information
- **Function**: Searches for specific legal terms, cases, or concepts and summarizes findings
- **Features**:
  - Uses WebSearchTool for comprehensive research
  - Produces concise 2-3 paragraph summaries (under 300 words)
  - Focuses on key legal principles, holdings, and relevant facts
  - Designed for legal professionals synthesizing briefs or memorandums

### 3. LegalWriterAgent (`writer_agent.py`)
- **Purpose**: Synthesizes research into professional legal documents
- **Function**: Creates comprehensive legal memorandums or briefs
- **Output**:
  - Structured legal analysis (Introduction, Facts, Issues, Analysis, Conclusion)
  - Markdown-formatted reports with proper legal citations
  - Short summaries and follow-up questions for further research
- **Model**: Uses `o3` for sophisticated legal writing and analysis

## System Workflow

1. **Planning**: User enters a legal query, and the LegalPlannerAgent creates a comprehensive research strategy
2. **Research**: Multiple LegalSearchAgents run in parallel to gather information from web searches
3. **Synthesis**: LegalWriterAgent creates a final legal memorandum or brief with proper structure and citations

## Key Features

- **Legal-Specific Intelligence**: All agents are specifically trained and prompted for legal research tasks
- **Parallel Processing**: Multiple search agents work simultaneously for faster results
- **Professional Output**: Generates properly structured legal documents with citations
- **Comprehensive Coverage**: Searches for case law, statutes, legal precedents, and doctrines
- **Interactive Tracing**: Built-in trace ID generation for monitoring the research process

## Sample Legal Queries

This system can handle various types of legal research:
- Constitutional law questions
- Contract interpretation issues
- Tort liability analysis
- Criminal law precedents
- Corporate governance matters
- Intellectual property disputes

## Suggested Improvements for Legal Practice

If you're building your own legal research system, consider these enhancements:

1. **Legal Database Integration**: Add support for fetching information from Westlaw, LexisNexis, or other legal databases
2. **Document Upload**: Allow users to attach case files, contracts, or other legal documents as baseline context
3. **Citation Verification**: Implement automated citation checking and formatting (Bluebook, etc.)
4. **Practice Area Specialization**: Create specialized agents for different areas of law (tax, patent, etc.)
5. **Legal Code Execution**: Allow running calculations for damages, interest, or statutory compliance
6. **Jurisdiction-Specific Research**: Tailor searches based on relevant jurisdictions and court levels
