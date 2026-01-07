# Mock RAGFlow Integration for InnerSource Hub PoC
# Simulates document ingestion and natural language search.

import random

class RAGFlowMock:
    def __init__(self):
        self.documents = {}

    def ingest_project(self, project_id: int, vcs_url: str):
        """
        Simulates ingesting project documentation (README.md, ARCHITECTURE.md) from a VCS URL.
        """
        print(f"MOCK: Ingesting documentation for project {project_id} from {vcs_url}")
        self.documents[project_id] = f"Indexed content from {vcs_url}"
        return {"status": "success", "message": f"Project {project_id} ingested."}

    def search(self, query: str, projects):
        """
        Simulates a natural language search.
        Returns a list of relevant projects with a reason.
        """
        print(f"MOCK: Searching for '{query}'")

        # Simple keyword matching simulation or random selection for PoC
        results = []
        for project in projects:
            # Simulate relevance based on random chance or keyword match in description
            score = 0
            if query.lower() in project.description.lower() or query.lower() in project.problem_statement.lower():
                score = 0.9
            elif query.lower() in (project.tags or "").lower():
                score = 0.8
            else:
                 # Random chance to include some projects for demonstration purposes
                 if random.random() > 0.7:
                     score = 0.5 + (random.random() * 0.4)

            if score > 0.5:
                results.append({
                    "project": project,
                    "score": score,
                    "reason": f"Matches terms in {random.choice(['description', 'problem statement', 'tags'])}"
                })

        results.sort(key=lambda x: x["score"], reverse=True)
        return results

ragflow_client = RAGFlowMock()
