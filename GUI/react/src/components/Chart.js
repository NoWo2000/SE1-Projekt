import React from 'react';
import CanvasJSChart from '../lib/canvasjs.react';

class Chart extends React.Component {

    render() {
        var datapoints = [];
        this.props.data.forEach(alarm => {
            datapoints.push({
                x: alarm.date,
                y: alarm.probability,
                color: (alarm.probability >= 95 ? "#E94D4D" : (alarm.probability >= 85 ? "#FF994F" : (alarm.probability >= 75 ? "#EDC535" : "#4A73B0"))),
                toolTipContent: (function () {
                    let date = new Date(alarm.date);
                    let hours = date.getHours();
                    let minutes = date.getMinutes();
                    let seconds = date.getSeconds();
                    let time = (hours < 10 ? "0" + hours.toString() : hours.toString()) + ":" + (minutes < 10 ? "0" + minutes.toString() : minutes.toString()) + ":" + (seconds < 10 ? "0" + seconds.toString() : seconds.toString());
                    return "Alarm: #" + alarm.id.toString() + "<br/>" + time;
                }())
            });
        });
        const options = {
            animationEnabled: false,
            exportEnabled: true,
            theme: "light1",
            title: {
                text: "Today's Events/Alarms",
                fontFamily: "open sans",
                fontSize: 30
            },
            axisX: {
                minimum: (function () { try { console.log("try"); return (+ new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate())); } catch (e) { console.log("catch"); return 0 } }()),
                maximum: (function () { try { console.log("try"); return (+ new Date(new Date().getFullYear(), new Date().getMonth(), new Date().getDate(), 23, 59, 59)); } catch (e) { console.log("catch"); return 0 } }())
            },
            axisY: {
                title: "Probability",
                titleFontSize: 30,
                titleFontWeight: "regular",
                gridThickness: 0,
                includeZero: true,
                maximum: 100,
                stripLines: [
                    {
                        startValue: 75,
                        endValue: 75.5,
                        color: "#EDC535"
                    },
                    {
                        startValue: 85,
                        endValue: 85.5,
                        color: "#FF994F"
                    },
                    {
                        startValue: 95,
                        endValue: 95.5,
                        color: "#E94D4D"
                    },

                ]
            },
            dataPointMinWidth: 5,
            height: 720,
            data: [{
                type: "scatter",
                xValueType: "dateTime",
                dataPoints: datapoints
            }]
        }

        return (
            <div className="border">
                <CanvasJSChart options={options} />
                {console.log(options.axisX)}
            </div >
        );
    }
}

export default Chart;  