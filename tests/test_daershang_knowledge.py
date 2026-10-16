"""
Year 2 Semester 1 ("大二上") Curriculum Knowledge Graph & Ontologies Verification Suite
Tests the 5 core subjects:
  1. Operations Research (or)
  2. Management Information Systems (mis)
  3. Probability & Mathematical Statistics (prob_stat)
  4. Marketing Management (mkt)
  5. Academic English & Communication (eng)
"""

import pytest
from typing import Dict, Any, List
from starlette.testclient import TestClient
from backend.app.data.daershang_knowledge import (
    DAERSHANG_SUBJECTS,
    DAERSHANG_KNOWLEDGE_MAP,
    OR_CONCEPTS,
    MIS_CONCEPTS,
    PROB_STAT_CONCEPTS,
    MKT_CONCEPTS,
    ENG_CONCEPTS
)
from backend.app.services.knowledge_service import knowledge_service


# -----------------------------------------------------------------------------
# 1. Domain Data Integrity Tests
# -----------------------------------------------------------------------------

def test_daershang_subjects_count():
    """Verify all 5 Year 2 Semester 1 subjects are registered."""
    codes = {s.code for s in DAERSHANG_SUBJECTS}
    assert codes == {"or", "mis", "prob_stat", "mkt", "eng"}, f"Unexpected subject codes: {codes}"
    for s in DAERSHANG_SUBJECTS:
        assert s.semester == "大二上"
        assert len(s.name) > 0
        assert len(s.description) > 0


@pytest.mark.parametrize("subj_code,expected_concepts", [
    ("or", OR_CONCEPTS),
    ("mis", MIS_CONCEPTS),
    ("prob_stat", PROB_STAT_CONCEPTS),
    ("mkt", MKT_CONCEPTS),
    ("eng", ENG_CONCEPTS),
])
def test_subject_concepts_and_traps(subj_code: str, expected_concepts: list):
    """Verify each discipline possesses detailed concepts with prerequisites and misconception traps."""
    assert len(expected_concepts) >= 4, f"Discipline {subj_code} should have at least 4 core concepts"
    for concept in expected_concepts:
        assert concept.subject == subj_code
        assert len(concept.id) > 0
        assert len(concept.label) > 0
        assert len(concept.definition) > 10, f"Concept definition too short: {concept.label}"
        assert len(concept.prerequisites) > 0, f"Concept {concept.label} should list prerequisites"
        assert len(concept.traps) > 0, f"Concept {concept.label} should list distractor traps"


@pytest.mark.parametrize("subj_code", ["or", "mis", "prob_stat", "mkt", "eng"])
def test_graph_topology_integrity(subj_code: str):
    """Verify that topological graph nodes and edges have valid IDs and directional links."""
    entry = DAERSHANG_KNOWLEDGE_MAP[subj_code]
    graph = entry["graph"]

    assert len(graph.nodes) >= 4, f"Graph for {subj_code} must have at least 4 nodes"
    assert len(graph.edges) >= 3, f"Graph for {subj_code} must have at least 3 edges"

    node_ids = {n.id for n in graph.nodes}
    assert len(node_ids) == len(graph.nodes), f"Duplicate node IDs in graph for {subj_code}"

    # Verify every edge connects valid nodes
    for edge in graph.edges:
        assert edge.from_node in node_ids, f"Edge from_node '{edge.from_node}' not found in nodes of {subj_code}"
        assert edge.to_node in node_ids, f"Edge to_node '{edge.to_node}' not found in nodes of {subj_code}"
        assert len(edge.label) > 0, f"Edge label cannot be empty in {subj_code}"


# -----------------------------------------------------------------------------
# 2. REST API Endpoint Tests (/api/knowledge/...)
# -----------------------------------------------------------------------------

def test_api_list_subjects(client: TestClient):
    """Verify GET /api/knowledge/subjects returns baseline plus Daershang subjects."""
    resp = client.get("/api/knowledge/subjects")
    assert resp.status_code == 200
    data = resp.json()

    assert "total" in data
    assert "subjects" in data
    assert data["total"] >= 9  # 4 baseline + 5 daershang

    codes = [s["code"] for s in data["subjects"]]
    for expected in ["or", "mis", "prob_stat", "mkt", "eng", "law", "cs", "econ", "se"]:
        assert expected in codes, f"Expected subject '{expected}' missing from /api/knowledge/subjects"


def test_api_list_subjects_filter_semester(client: TestClient):
    """Verify filtering subjects by semester='大二上'."""
    resp = client.get("/api/knowledge/subjects?semester=大二上")
    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] == 5
    codes = {s["code"] for s in data["subjects"]}
    assert codes == {"or", "mis", "prob_stat", "mkt", "eng"}


@pytest.mark.parametrize("subj_alias,expected_code", [
    ("or", "or"),
    ("operations_research", "or"),
    ("运筹学", "or"),
    ("mis", "mis"),
    ("管理信息系统", "mis"),
    ("prob_stat", "prob_stat"),
    ("概率论与数理统计", "prob_stat"),
    ("数学", "prob_stat"),
    ("mkt", "mkt"),
    ("市场营销学", "mkt"),
    ("eng", "eng"),
    ("学术英语", "eng"),
    ("law", "law"),
    ("se", "se")
])
def test_api_get_knowledge_graph_success(client: TestClient, subj_alias: str, expected_code: str):
    """Verify GET /api/knowledge/graph with both canonical codes and aliases."""
    resp = client.get(f"/api/knowledge/graph?subject={subj_alias}")
    assert resp.status_code == 200, f"Failed for subject query: {subj_alias}"
    data = resp.json()

    assert data["subject"] == expected_code
    assert "graph" in data
    assert "nodes" in data["graph"]
    assert "edges" in data["graph"]
    assert len(data["graph"]["nodes"]) > 0
    assert "concepts" in data
    assert len(data["concepts"]) > 0


def test_api_get_knowledge_graph_not_found(client: TestClient):
    """Verify querying an invalid subject returns 404 rather than 500 error."""
    resp = client.get("/api/knowledge/graph?subject=nonexistent_astronomy_999")
    assert resp.status_code == 404


def test_api_search_concepts(client: TestClient):
    """Verify GET /api/knowledge/concepts searches definitions, traps, and prerequisites."""
    # Search for Bayes
    resp = client.get("/api/knowledge/concepts?query=贝叶斯")
    assert resp.status_code == 200
    results = resp.json()
    assert isinstance(results, list)
    assert len(results) >= 1
    assert any("贝叶斯" in c["label"] or "贝叶斯" in c["definition"] for c in results)

    # Search for C2M
    resp_c2m = client.get("/api/knowledge/concepts?query=C2M")
    assert resp_c2m.status_code == 200
    results_c2m = resp_c2m.json()
    assert len(results_c2m) >= 1
    assert any("C2M" in c["label"] or "C2M" in c["definition"] for c in results_c2m)
