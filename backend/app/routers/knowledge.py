"""
Knowledge Router - GET /api/knowledge/subjects, GET /api/knowledge/graph, GET /api/knowledge/concepts
Provides multi-discipline curriculum graph topologies and Year 2 Semester 1 ("大二上") knowledge ontologies.
"""

from typing import List, Optional
from fastapi import APIRouter, Query, HTTPException, status
from backend.app.models.knowledge import SubjectListResponse, KnowledgeGraphResponse, ConceptDetail
from backend.app.services.knowledge_service import knowledge_service

router = APIRouter()


@router.get("/knowledge/subjects", response_model=SubjectListResponse, tags=["Knowledge"])
def list_subjects(
    category: Optional[str] = Query(None, description="Filter by category (stem, business, humanities)"),
    semester: Optional[str] = Query(None, description="Filter by semester (e.g. '大二上')")
) -> SubjectListResponse:
    """
    List all supported academic disciplines.
    Returns curriculum metadata including Year 2 Semester 1 ('大二上') course modules.
    """
    return knowledge_service.list_all_subjects(category=category, semester=semester)


@router.get("/knowledge/graph", response_model=KnowledgeGraphResponse, tags=["Knowledge"])
def get_subject_knowledge_graph(
    subject: str = Query(..., description="Canonical discipline code or alias (e.g. or, mis, prob_stat, mkt, eng, law, cs, econ, se)")
) -> KnowledgeGraphResponse:
    """
    Retrieve topological knowledge graph for a specified subject.
    Contains core concepts, prerequisite dependency links, and distractor misconception nodes.
    """
    result = knowledge_service.get_subject_knowledge_graph(subject=subject)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Knowledge graph for subject '{subject}' not found or unrecognized."
        )
    return result


@router.get("/knowledge/concepts", response_model=List[ConceptDetail], tags=["Knowledge"])
def search_curriculum_concepts(
    query: str = Query(..., min_length=1, description="Keyword search term"),
    subject: Optional[str] = Query(None, description="Optional discipline code constraint")
) -> List[ConceptDetail]:
    """
    Search curriculum concepts, definitions, prerequisite theorems and trap links across subjects.
    """
    return knowledge_service.search_concepts(query=query, subject=subject)
