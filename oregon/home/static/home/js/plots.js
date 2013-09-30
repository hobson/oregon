function draw(data) { "use strict";
    d3.select("body")
        .append("ul")
        .selectAll("li")
        .data(data)
        .enter()
        .append("li")
            .text(function (d) {
                return "no" + d;
            });
}