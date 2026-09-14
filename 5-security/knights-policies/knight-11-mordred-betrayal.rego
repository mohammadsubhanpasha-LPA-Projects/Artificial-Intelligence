package knight.mordred

violation[msg] {
    input.request.kind.kind == "Deployment"
    # Check the custom annotation that trivy has signed off on 0 criticals
    not input.request.object.metadata.annotations["trivy.critical"] == "0"
    msg = "Deny if image has CRITICAL CVE: trivy.critical must be 0"
}
