package knight.kay

violation[msg] {
    input.request.kind.kind == "Deployment"
    msg = "Deny if no NetworkPolicy"
    not has_network_policy
}

has_network_policy {
    # In a real environment, you'd check the cluster state.
    input.request.object.metadata.annotations["has-network-policy"] == "true"
}
