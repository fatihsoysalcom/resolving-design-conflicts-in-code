import json

# Represents a feature with its requirements and technical constraints.
class Feature:
    def __init__(self, name, requirements, technical_constraints):
        self.name = name
        self.requirements = requirements  # e.g., {'user_story': 'As a user, I want to...'} 
        self.technical_constraints = technical_constraints # e.g., {'performance': 'must be < 100ms', 'integration': 'must use existing API X'}

    def __str__(self):
        return f"Feature: {self.name}\n  Requirements: {self.requirements}\n  Constraints: {self.technical_constraints}"

# Represents a potential conflict between two features or a feature and a system aspect.
class DesignConflict:
    def __init__(self, description, conflicting_features, resolution_strategy=None):
        self.description = description
        self.conflicting_features = conflicting_features # List of Feature objects or feature names
        self.resolution_strategy = resolution_strategy # Proposed solution

    def __str__(self):
        feature_names = [f.name if isinstance(f, Feature) else f for f in self.conflicting_features]
        return f"Conflict: {self.description}\n  Affects: {', '.join(feature_names)}\n  Resolution: {self.resolution_strategy or 'Unresolved'}"

# --- Simulation of a development scenario with conflicts ---

# Define some features
user_auth = Feature(
    name="User Authentication",
    requirements={'user_story': 'As a user, I want to log in securely'},
    technical_constraints={'security': 'use OAuth 2.0', 'performance': 'login < 500ms'}
)

realtime_dashboard = Feature(
    name="Realtime Dashboard",
    requirements={'user_story': 'As an admin, I want to see live updates'},
    technical_constraints={'performance': 'updates < 100ms', 'integration': 'use WebSockets'}
)

# --- Identifying potential conflicts ---

conflicts = []

# Conflict 1: Performance requirements clash
if user_auth.technical_constraints.get('performance') < realtime_dashboard.technical_constraints.get('performance'):
    conflicts.append(DesignConflict(
        description="Realtime dashboard performance requirement is too strict for user authentication overhead.",
        conflicting_features=[user_auth, realtime_dashboard],
        resolution_strategy="Optimize dashboard update frequency or use separate connection pools."
    ))

# Conflict 2: Integration mismatch (hypothetical)
# Imagine a new feature requiring an old, incompatible API.
legacy_reporting = Feature(
    name="Legacy Reporting",
    requirements={'user_story': 'As a manager, I need old reports'},
    technical_constraints={'integration': 'uses deprecated API v1'}
)

new_analytics = Feature(
    name="New Analytics",
    requirements={'user_story': 'As an analyst, I need advanced analytics'},
    technical_constraints={'integration': 'requires API v2'}
)

if legacy_reporting.technical_constraints['integration'] != new_analytics.technical_constraints['integration']:
    conflicts.append(DesignConflict(
        description="New analytics feature cannot integrate with legacy reporting API.",
        conflicting_features=[legacy_reporting, new_analytics],
        resolution_strategy="Develop an adapter layer or migrate legacy reporting to v2."
    ))

# --- Presenting the conflicts and resolutions ---

print("--- Identified Design Conflicts ---")
if not conflicts:
    print("No significant design conflicts found.")
else:
    for conflict in conflicts:
        print(conflict)
        print("---")

print("\n--- Resolution Strategy ---")
print("When design conflicts arise, it's crucial to:")
print("1. Clearly define the conflicting requirements/constraints.")
print("2. Facilitate open communication between teams (e.g., Dev, UX, Product).")
print("3. Explore alternative solutions and their trade-offs.")
print("4. Document the chosen resolution and its implications.")
print("5. Re-evaluate and iterate as needed.")
