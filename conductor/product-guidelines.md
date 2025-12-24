# Product Guidelines - EYE

## Voice & Tone
- **Professional and Precise:** Communication must be clinically accurate, clear, and objective, utilizing standard medical terminology appropriate for ophthalmologists and doctors.

## Trust & Verification
- **Explicit Citations:** All extracted data points must be traceable back to their source in the clinical notes to ensure verifiability.
- **Confidence Scoring:** The system will provide visual confidence indicators for extracted entities to flag potential uncertainties.
- **Human-in-the-Loop:** A mandatory verification step is required for doctors to review and approve extracted data before final submission.

## User Interface Design
- **Visual Hierarchy:** Prioritize clarity through distinct headings, color-coding for critical findings/abnormalities, and bold text for key information to facilitate rapid scanning by busy professionals.

## Privacy, Security & Compliance (LGPD/HIPAA)
- **Medical Confidentiality is Paramount:** All architectural and design decisions must prioritize the protection of patient data above all else.
- **Local-First Processing:** Leverage local inference (e.g., Ollama, llama-cpp) whenever possible to prevent sensitive data from leaving the secure environment.
- **Strict Audit Logging:** Maintain immutable logs of every data access, modification, and export event, recording timestamp and user identity.
- **Anonymization by Default:** Implement rigorous automatic redaction of PII (Personally Identifiable Information) before any data is subjected to external processing, if strictly necessary.
