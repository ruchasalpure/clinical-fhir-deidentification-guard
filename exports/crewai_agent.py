from crewai import Agent

clinical_fhir_deidentification_guard = Agent(
    role="Clinical Fhir Deidentification Guard",
    goal="Deliver high-precision autonomous Clinical Fhir Deidentification Guard operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
