"""
Knowledge Domain Schemas and Models
Pydantic v2 compatible schemas with bidirectional camelCase / snake_case support.
Supports multi-discipline knowledge graphs, prerequisite topologies, and misconception traps.
"""

from typing import List, Dict, Optional, Any
from pydantic import Field
from backend.app.models.common import CamelModel
from backend.app.models.quiz import GraphNode, GraphEdge, GraphData, TrapDetail


class SubjectMeta(CamelModel):
    """Subject/Discipline metadata and taxonomy description."""
    code: str = Field(..., description="Canonical discipline code (e.g. or, mis, prob_stat, mkt, eng, law, cs, econ, se)")
    name: str = Field(..., description="Display discipline name in Chinese")
    name_en: str = Field("", description="Display discipline name in English")
    badge: str = Field("", description="Curriculum badge or examination tag")
    category: str = Field("core", description="Discipline category (core, stem, business, humanities)")
    semester: str = Field("大二上", description="Academic term or level, e.g. '大二上', '通识基础'")
    icon: str = Field("📚", description="Emoji icon for UI presentation")
    description: str = Field("", description="Discipline curriculum overview")


class ConceptDetail(CamelModel):
    """Fine-grained curriculum concept entity with prerequisite and misconception links."""
    id: str = Field(..., description="Unique concept identifier (e.g. or_c1, mis_c2)")
    label: str = Field(..., description="Concept title")
    subject: str = Field(..., description="Subject code")
    definition: str = Field(..., description="Authoritative definition and academic explanation")
    prerequisites: List[str] = Field(default_factory=list, description="IDs or names of prerequisite theorems/concepts")
    traps: List[str] = Field(default_factory=list, description="Associated misconception trap titles or IDs")
    applications: List[str] = Field(default_factory=list, description="Practical real-world engineering or business scenarios")


class KnowledgeGraphResponse(CamelModel):
    """Response containing topological graph nodes, directed edges, and metadata for a subject."""
    subject: str = Field(..., description="Canonical discipline code")
    subject_name: str = Field(..., description="Discipline name")
    graph: GraphData = Field(..., description="Complete topological concept graph")
    concepts: List[ConceptDetail] = Field(default_factory=list, description="Detailed concept cards")
    total_concepts: int = Field(0, description="Total number of concept nodes")
    total_edges: int = Field(0, description="Total number of prerequisite / trap edges")


class SubjectListResponse(CamelModel):
    """List of all supported academic subjects with curriculum metadata."""
    total: int = Field(..., description="Total count of registered subjects")
    subjects: List[SubjectMeta] = Field(..., description="List of registered subject metadata")
