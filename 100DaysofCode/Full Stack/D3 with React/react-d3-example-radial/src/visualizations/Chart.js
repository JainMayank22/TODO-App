import React, { Component } from "react";
import * as d3 from "d3";

const width = 650;
const height = 650;
const margin = { top: 20, right: 5, bottom: 20, left: 35 };

class Chart extends Component {
  state = {
    slices: []
  };

  static getDerivedStateFromProps(nextProps, prevState) {
    const { data } = nextProps;
    if (!data) return {};
    const radiusScale = d3.scaleLinear().range([0, width / 2]);
    const colorScale = d3.scaleSequential(d3.interpolateSpectral);

    const tempMax = d3.max(data, (d) => d.high);
    const [minAvg, maxAvg] = d3.extent(data, (d) => d.avg);
    radiusScale.domain([0, tempMax]);
    colorScale.domain([maxAvg, minAvg]);

    // one arc per day, innerRadius is low temp, outerRadius is high temp
    const arcGenerator = d3.arc();
    const perSliceAngle = (2 * Math.PI) / data.length;
    const slices = data.map((d, i) => {
      return {
        fill: colorScale(d.avg),
        path: arcGenerator({
          startAngle: i * perSliceAngle,
          endAngle: (i + 1) * perSliceAngle,
          innerRadius: radiusScale(d.low),
          outerRadius: radiusScale(d.high)
        })
      };
    });

    return { slices };
  }

  render() {
    return (
      <svg width={width} height={height}>
        <g transform={`translate(${width / 2}, ${height / 2})`}>
          {this.state.slices.map((d) => (
            <path d={d.path} fill={d.fill} />
          ))}
        </g>
      </svg>
    );
  }
}

export default Chart;
